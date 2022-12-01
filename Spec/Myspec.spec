<?xml version="1.0" encoding="UTF-8"?>
<SpecificationProfile version="1.3" name="">
	<General>
		<InfoGroups name="origin">
			<InfoGroup name="creator">
				<Info name="name">BTC EmbeddedPlatform Application</Info>
				<Info name="version">2.5p0</Info>
				<Info name="date">29-Nov-2019</Info>
			</InfoGroup>
			<InfoGroup name="user">
				<Info name="name">leifdriebold</Info>
				<Info name="date">Mo 18. Nov 16:45:41 2019</Info>
			</InfoGroup>
		</InfoGroups>
	</General>
	<Design>
		<Components>
			<Component name="power_window_controller" id="ComponentID1" parent="" sampleTime="0.01" />
		</Components>
	</Design>
	<Universe>
		<SpecificationVariableGroups name="variables" component="ComponentID1">
			<SpecificationVariableGroup name="input" />
			<SpecificationVariableGroup name="output" />
			<SpecificationVariableGroup name="local" />
			<SpecificationVariableGroup name="calibration" />
			<SpecificationVariableGroup name="macro">
				<SpecificationVariable name="obstacleIsDetected" id="ComponentID1VariableID1">
					<SpecificationVariableAttribute name="definition">detection_obstacle</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)obstacle is detected(...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="20" offset="6" name="reference">InformalRequirement::REQ_PW_4_1</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
				<SpecificationVariable name="movingDown" id="ComponentID1VariableID2">
					<SpecificationVariableAttribute name="definition">Sa1_move_down</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)moving down(...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="12" offset="52" name="reference">InformalRequirement::REQ_PW_4_1</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
				<SpecificationVariable name="_10ms" id="ComponentID1VariableID3">
					<SpecificationVariableAttribute name="definition">10</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)10 [ms](...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="7" offset="77" name="reference">InformalRequirement::REQ_PW_4_1</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
				<SpecificationVariable name="movingUp" id="ComponentID1VariableID4">
					<SpecificationVariableAttribute name="definition">Sa1_move_up</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)moving up(...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
				<SpecificationVariable name="driverUp" id="ComponentID1VariableID5">
					<SpecificationVariableAttribute name="definition">Sa1_driver_up</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)driver up(...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
			</SpecificationVariableGroup>
		</SpecificationVariableGroups>
	</Universe>
	<Assumptions>
		<AssumptionGroup name="assumptions" component="ComponentID1">
			<Assumption id="ComponentID1AssumptionID1" parent="" patternRef="7c085862-8e56-4e7d-a889-8ffc53c4e497">
				<InfoGroup name="informal">
					<Info name="name">EnvironmentalAssumption</Info>
					<Info name="description" />
				</InfoGroup>
				<FormalAssumption id="ComponentID1FormalAssumptionID1" specId="SPECID:SUP:V1.0">
					<ParameterGroup name="parameters">
						<Parameter name="interpretation">2</Parameter>
						<Parameter name="activation_mode">3</Parameter>
						<Parameter name="startup_phase">1</Parameter>
						<Parameter name="GlobalScope">ms</Parameter>
						<Parameter name="GlobalScope_isInf">1</Parameter>
						<Parameter name="ActionExitCond">0</Parameter>
						<Parameter name="TriggerExitCond">0</Parameter>
						<Parameter name="ActionEndEv">$movingUp</Parameter>
						<Parameter name="startup_n">0ms</Parameter>
						<Parameter name="startup_delay">0</Parameter>
						<Parameter name="ActionStartEvMax">0ms</Parameter>
						<Parameter name="ActionStartEvMax_isInf">0</Parameter>
						<Parameter name="TriggerMin">0ms</Parameter>
						<Parameter name="TriggerMin_isInf">0</Parameter>
						<Parameter name="ActionMax">0ms</Parameter>
						<Parameter name="ActionMax_isInf">0</Parameter>
						<Parameter name="TriggerStartEv">$driverUp</Parameter>
						<Parameter name="TriggerCond">$driverUp</Parameter>
						<Parameter name="ActionCond">$movingUp</Parameter>
						<Parameter name="TriggerEndEv">$driverUp</Parameter>
						<Parameter name="ActionStartEv">$movingUp</Parameter>
						<Parameter name="startup_R">1</Parameter>
						<Parameter name="cycle_delay">0</Parameter>
						<Parameter name="TriggerMax">0ms</Parameter>
						<Parameter name="TriggerMax_isInf">0</Parameter>
						<Parameter name="ActionStartEvMin">0ms</Parameter>
						<Parameter name="ActionMin">0ms</Parameter>
						<Parameter name="ActionMin_isInf">0</Parameter>
					</ParameterGroup>
				</FormalAssumption>
			</Assumption>
		</AssumptionGroup>
	</Assumptions>
	<Specifications>
		<SpecificationGroup name="specifications" component="ComponentID1">
			<Specification id="ComponentID1SpecificationID1" parent="" patternRef="7792a12a-3add-4ee4-9408-9c1fd747464a">
				<InfoGroup name="informal">
					<Info name="name">F_REQ_PW_4_1</Info>
					<Info name="description">If an obstacle is detected, the window has to start moving down in less than 10 [ms]. 
Pre-Condition: N/A</Info>
				</InfoGroup>
				<FormalSpecification id="ComponentID1FormalSpecificationID3" specId="SPECID:SUP:V1.0">
					<ParameterGroup name="parameters">
						<Parameter name="interpretation">2</Parameter>
						<Parameter name="activation_mode">3</Parameter>
						<Parameter name="startup_phase">1</Parameter>
						<Parameter name="GlobalScope">ms</Parameter>
						<Parameter name="GlobalScope_isInf">1</Parameter>
						<Parameter name="ActionExitCond">0</Parameter>
						<Parameter name="TriggerExitCond">0</Parameter>
						<Parameter name="ActionEndEv">$movingDown</Parameter>
						<Parameter name="startup_n">0ms</Parameter>
						<Parameter name="startup_delay">0</Parameter>
						<Parameter name="ActionStartEvMax">$_10msms</Parameter>
						<Parameter name="ActionStartEvMax_isInf">0</Parameter>
						<Parameter name="TriggerMin">0ms</Parameter>
						<Parameter name="TriggerMin_isInf">0</Parameter>
						<Parameter name="ActionMax">0ms</Parameter>
						<Parameter name="ActionMax_isInf">0</Parameter>
						<Parameter name="TriggerStartEv">$obstacleIsDetected</Parameter>
						<Parameter name="TriggerCond">$obstacleIsDetected</Parameter>
						<Parameter name="ActionCond">$movingDown</Parameter>
						<Parameter name="TriggerEndEv">$obstacleIsDetected</Parameter>
						<Parameter name="ActionStartEv">$movingDown</Parameter>
						<Parameter name="startup_R">1</Parameter>
						<Parameter name="cycle_delay">0</Parameter>
						<Parameter name="TriggerMax">0ms</Parameter>
						<Parameter name="TriggerMax_isInf">0</Parameter>
						<Parameter name="ActionStartEvMin">0ms</Parameter>
						<Parameter name="ActionMin">0ms</Parameter>
						<Parameter name="ActionMin_isInf">0</Parameter>
					</ParameterGroup>
					<FormalAssumptions>
						<FormalAssumptionLinkGroup name="pattern">
							<FormalAssumptionLink formalAssumption="ComponentID1FormalAssumptionID1" active="1" />
						</FormalAssumptionLinkGroup>
					</FormalAssumptions>
				</FormalSpecification>
			</Specification>
		</SpecificationGroup>
	</Specifications>
	<Requirements>
		<RequirementsGroup component="ComponentID1" name="requirement">
			<Requirement id="ComponentID1RequirementID1" parent="" uuid="InformalRequirement::REQ_PW_4_1">
				<InfoGroup name="origin">
					<Info name="externalID">InformalRequirement</Info>
					<Info name="name">REQ_PW_4_1</Info>
					<Info name="description">If an obstacle is detected, the window has to start moving down in less than 10 [ms]. 
Pre-Condition: N/A</Info>
					<Info name="externalURI">file:/C:/01_Arbeit/PowerWindow/Requirements_PowerWindow%20-%20WithHierarchy.xls#InformalRequirement!A7</Info>
					<Info name="groupName">InformalRequirement</Info>
				</InfoGroup>
				<SpecificationLinkGroup name="specifications">
					<SpecificationLink specification="ComponentID1PatternId1" />
				</SpecificationLinkGroup>
			</Requirement>
		</RequirementsGroup>
	</Requirements>
	<Patterns>
		<PatternGroup name="patterns" component="ComponentID1">
			<Pattern id="ComponentID1PatternId1" uuid="7792a12a-3add-4ee4-9408-9c1fd747464a">
				<InfoGroup name="informal">
					<Info name="name">Pattern3</Info>
					<Info name="description" />
					<Info name="reference_length">105</Info>
					<Info name="reference_offset">0</Info>
				</InfoGroup>
				<FormalPattern id="ComponentID1FormalSpecificationID1" specId="SPECID:SUP:V1.0">
					<ParameterGroup name="parameters">
						<Parameter name="interpretation">2</Parameter>
						<Parameter name="activation_mode">3</Parameter>
						<Parameter name="startup_phase">1</Parameter>
						<Parameter name="GlobalScope">ms</Parameter>
						<Parameter name="GlobalScope_isInf">1</Parameter>
						<Parameter name="ActionExitCond">0</Parameter>
						<Parameter name="TriggerExitCond">0</Parameter>
						<Parameter name="ActionEndEv">$movingDown</Parameter>
						<Parameter name="startup_n">0ms</Parameter>
						<Parameter name="startup_delay">0</Parameter>
						<Parameter name="ActionStartEvMax">$_10msms</Parameter>
						<Parameter name="ActionStartEvMax_isInf">0</Parameter>
						<Parameter name="TriggerMin">0ms</Parameter>
						<Parameter name="TriggerMin_isInf">0</Parameter>
						<Parameter name="ActionMax">0ms</Parameter>
						<Parameter name="ActionMax_isInf">0</Parameter>
						<Parameter name="TriggerStartEv">$obstacleIsDetected</Parameter>
						<Parameter name="TriggerCond">$obstacleIsDetected</Parameter>
						<Parameter name="ActionCond">$movingDown</Parameter>
						<Parameter name="TriggerEndEv">$obstacleIsDetected</Parameter>
						<Parameter name="ActionStartEv">$movingDown</Parameter>
						<Parameter name="startup_R">1</Parameter>
						<Parameter name="cycle_delay">0</Parameter>
						<Parameter name="TriggerMax">0ms</Parameter>
						<Parameter name="TriggerMax_isInf">0</Parameter>
						<Parameter name="ActionStartEvMin">0ms</Parameter>
						<Parameter name="ActionMin">0ms</Parameter>
						<Parameter name="ActionMin_isInf">0</Parameter>
					</ParameterGroup>
				</FormalPattern>
			</Pattern>
			<Pattern id="ComponentID1PatternId2" uuid="7c085862-8e56-4e7d-a889-8ffc53c4e497">
				<InfoGroup name="informal">
					<Info name="name">EnvironmentalAssumption</Info>
					<Info name="description" />
					<Info name="reference_length" />
					<Info name="reference_offset" />
				</InfoGroup>
				<FormalPattern id="ComponentID1FormalSpecificationID2" specId="SPECID:SUP:V1.0">
					<ParameterGroup name="parameters">
						<Parameter name="interpretation">2</Parameter>
						<Parameter name="activation_mode">3</Parameter>
						<Parameter name="startup_phase">1</Parameter>
						<Parameter name="GlobalScope">ms</Parameter>
						<Parameter name="GlobalScope_isInf">1</Parameter>
						<Parameter name="ActionExitCond">0</Parameter>
						<Parameter name="TriggerExitCond">0</Parameter>
						<Parameter name="ActionEndEv">$movingUp</Parameter>
						<Parameter name="startup_n">0ms</Parameter>
						<Parameter name="startup_delay">0</Parameter>
						<Parameter name="ActionStartEvMax">0ms</Parameter>
						<Parameter name="ActionStartEvMax_isInf">0</Parameter>
						<Parameter name="TriggerMin">0ms</Parameter>
						<Parameter name="TriggerMin_isInf">0</Parameter>
						<Parameter name="ActionMax">0ms</Parameter>
						<Parameter name="ActionMax_isInf">0</Parameter>
						<Parameter name="TriggerStartEv">$driverUp</Parameter>
						<Parameter name="TriggerCond">$driverUp</Parameter>
						<Parameter name="ActionCond">$movingUp</Parameter>
						<Parameter name="TriggerEndEv">$driverUp</Parameter>
						<Parameter name="ActionStartEv">$movingUp</Parameter>
						<Parameter name="startup_R">1</Parameter>
						<Parameter name="cycle_delay">0</Parameter>
						<Parameter name="TriggerMax">0ms</Parameter>
						<Parameter name="TriggerMax_isInf">0</Parameter>
						<Parameter name="ActionStartEvMin">0ms</Parameter>
						<Parameter name="ActionMin">0ms</Parameter>
						<Parameter name="ActionMin_isInf">0</Parameter>
					</ParameterGroup>
				</FormalPattern>
			</Pattern>
		</PatternGroup>
	</Patterns>
</SpecificationProfile>
