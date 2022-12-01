from BTCRestApi import *
import time


"""------------------------------------------------------------------------------------"""
"""
Documentation notes on this file:

1) You will have to adjust some of the global config variables below, based on your own setup.

2) Throughout this code there are portions that have been commented out with multi-line comments.
These are not needed for the current workflow, but you may find them useful as you adapt and adjust
this program to better fit your own workflow. Feel free to uncomment and modify them as you please.
"""
"""------------------------------------------------------------------------------------"""

#### GLOBAL CONFIG VARIABLES
VERSION = '22.3p0'
EP_LOCATION = 'http://192.168.19.189:' #path to the REST server
PROFILE_PATH = 'e/profile.epp' # this points to a .epp profile FILE
MODEL_ROOT_LOCATION = 'e/PowerWindow_CCode/' # DIR where models reside
REPORT_EXPORT_DIR = "e/Reports/" # this is a DIRECTORY, not a file

ep = EPRestApi(8080, EP_LOCATION, VERSION) #the first attribute is the port on which the connection request will take place (default 8080)


#This is used to search a given ressource (based on JSON for a given key and returns the found value
def getkeyfromressource(key, ressource):
  return ressource.get(key)

# applying preferences to use the correct Matlab
preferences = \
  [
     { 'preferenceName': 'GENERAL_COMPILER_SETTING', 'preferenceValue': 'GCC64 (64bit)' }
]
ep.put_req('preferences', preferences) #only necessary for the first start

##########------------------- STEP 1: open existing project (optional) -------------------##########
# This step is optional in the container workflow
# open existing profile
#response = ep.get_req('profiles/' + PROFILE_PATH)


##########------------------- STEP 2: update architecture (only necessary after step 1) -------------------##########
#response = ep.put_req('architectures/')


# Alternatives in case you want to start from scratch without an existing profile
# Create a new profile and import a model architecture:
#
# -> 1: create a new profile
print("Step 1 creating profile")
firststart = time.time()
response = ep.post_req('profiles?discardCurrentProfile=true')
end = time.time()
print("Step 1 completed")
print("Duration (in seconds): ")
print(end - firststart)
print('\n')
#
# -> 2a: TargetLink Architecture import: This step is useful if we create a blank project.
# tl_import_payload = {
#     'tlModelFile': MODEL_ROOT_LOCATION + 'powerwindow_tl_v01.slx',
#     'tlInitScript': MODEL_ROOT_LOCATION + 'start.m'
# }
# response = ep.post_req('architectures/targetlink', tl_import_payload)

#
# -> 2b: Perform EmbeddedCoder architecture import: This step is useful if we create a blank project.
# ec_import_payload = {
#     'ecModelFile': MODEL_ROOT_LOCATION + 'powerwindow_ec.slx',
#     'ecInitScript': MODEL_ROOT_LOCATION + 'start.m'
# }
# response = ep.post_req('architectures/embedded-coder', ec_import_payload)
#
# -> 2c: Perform C-Code architecture import: This step is useful if we create a blank project.
print("Step 2 importing C architecture")
start = time.time()
c_import_payload={
    'modelFile': MODEL_ROOT_LOCATION + 'Codemodel_pwc.xml',
}
response = ep.post_req('architectures/ccode', c_import_payload)

response = ep.put_req('profiles', {
  'path': PROFILE_PATH
})
end = time.time()
print("Step 2 completed")
print("Duration (in seconds): ")
print(end - start)
print('\n')
##########------------------- STEP 3: Import Requirements -------------------##########
print("Step 3 importing requirements")
start = time.time()
excel_req_import_payload = {
  'kind': 'EXCEL',
  'nameAttribute': 'REQ_ID',
  'descriptionAttribute': 'Description',
  'additionalAttributes': [],
  'settings': [
    {
      'key': 'excel_file_path',
      'value': 'e/Requirements_PowerWindow.xlsx'
    },
    {
      'key': 'projectName_attr',
      'value': 'InformalRequirement'
    },
    {
      'key': 'excel_id_attr',
      'value': 'REQ_ID'
    }
  ]
}
reponse = ep.post_req('requirements-import', excel_req_import_payload)

requirementsource = getkeyfromressource('uid',ep.get_req('requirements-sources').json()[0])

print("Step 3 importing Spec file")
spec_import_payload = {
  'specPath': 'e/Spec/Myspec.spec',
}
response = ep.post_req('specifications-import', spec_import_payload)
end = time.time()
print("Step 3 completed")
print("Duration (in seconds): ")
print(end - start)
print('\n')
##########------------------- STEP 4: Importing Execution Records -------------------##########
print("Step 4 importing execution records")
start = time.time()
er_import_payload = {
  'paths': [
    'e/ERs/SIL_TestCase_failed.mdf',
    'e/ERs/SIL_TestCase_passed.mdf'
  ],
  'kind': "SIL",
  'csvDelimiter': "SEMICOLON"
}

response = ep.post_req('execution-records',er_import_payload)
end = time.time()
print("Step 4 completed")
print("Duration (in seconds): ")
print(end - start)
print('\n')
##########-----------
# -------- STEP 5: Executing Formal Test -------------------##########
print("Step 5 executing formal test")
start = time.time()
response = ep.post_req('execute-formal-test')
end = time.time()
print("Step 5 completed")
print("Duration (in seconds): ")
print(end - start)
print('\n')
##########------------------- STEP 6: Some reporting -------------------##########
print("Step 6 generating some reports")
start = time.time()
ft_report_creation_payload = {
  "executionConfigNames": [
    "SIL"
  ]
}
response = ep.post_req('requirements-sources/' + requirementsource + '/formal-test-reports',ft_report_creation_payload)
report_export_payload = {
  'exportPath': 'e/Reports'
}
report_id = getkeyfromressource('uid', response.json()[0])
response = ep.post_req('reports/'+report_id,report_export_payload)
end = time.time()
print("Step 6 completed")
print("Duration (in seconds): ")
print(end - start)
print('\n')
print("Finished with workflow.")
print("Saving profile.")
response = ep.put_req('profiles', {
  'path': PROFILE_PATH
})
end = time.time()
print("Complete workflow duration (in minutes): ")
print((end - firststart)/60)
print("Shutting down")
