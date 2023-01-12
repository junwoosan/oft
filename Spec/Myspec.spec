<?xml version="1.0" encoding="UTF-8"?>
<SpecificationProfile version="1.4" name="">
	<General>
		<InfoGroups name="origin">
			<InfoGroup name="creator">
				<Info name="name">BTC EmbeddedPlatform Application</Info>
				<Info name="version">22.3p0</Info>
				<Info name="date">25-Oct-2022</Info>
			</InfoGroup>
			<InfoGroup name="user">
				<Info name="name">forli</Info>
				<Info name="date">木 12. 1月 15:12:16 2023</Info>
			</InfoGroup>
		</InfoGroups>
	</General>
	<Design>
		<Components>
			<Component name="power_window_controller" id="ComponentID1" parent="/" sampleTime="0.01" />
		</Components>
	</Design>
	<Universe>
		<SpecificationVariableGroups name="variables" component="ComponentID1">
			<SpecificationVariableGroup name="input">
				<SpecificationVariable name="Sa1_driver_up" identifier="INPUT:Sa1_driver_up:var" id="ComponentID1VariableID1" />
				<SpecificationVariable name="Sa1_obstacle_position" identifier="INPUT:Sa1_obstacle_position:var" id="ComponentID1VariableID2" />
			</SpecificationVariableGroup>
			<SpecificationVariableGroup name="output">
				<SpecificationVariable name="Sa1_move_down" identifier="OUTPUT:Sa1_move_down:var" id="ComponentID1VariableID3" />
				<SpecificationVariable name="Sa1_obstacle_detection" identifier="OUTPUT:Sa1_obstacle_detection:var" id="ComponentID1VariableID4" />
				<SpecificationVariable name="Sa1_move_up" identifier="OUTPUT:Sa1_move_up:var" id="ComponentID1VariableID5" />
			</SpecificationVariableGroup>
			<SpecificationVariableGroup name="local">
				<SpecificationVariable name="detection_endstop_bottom" identifier="LOCAL:detection_endstop_bottom:var" id="ComponentID1VariableID6" />
			</SpecificationVariableGroup>
			<SpecificationVariableGroup name="calibration" />
			<SpecificationVariableGroup name="macro">
				<SpecificationVariable name="50Ms" id="ComponentID1VariableID7">
					<SpecificationVariableAttribute name="definition">50</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)50 [ms](...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="2" offset="83" name="reference">InformalRequirement::REQ_PW_1_1</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="7" offset="87" name="reference">InformalRequirement::REQ_PW_1_2</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
				<SpecificationVariable name="driverDown" id="ComponentID1VariableID8">
					<SpecificationVariableAttribute name="definition">Sa1_driver_up</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)driver down(...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="11" offset="7" name="reference">InformalRequirement::REQ_PW_1_2</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
				<SpecificationVariable name="notAtTheBottomEnd" id="ComponentID1VariableID9">
					<SpecificationVariableAttribute name="definition">!detection_endstop_bottom</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)not at the bottom end(...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
				<SpecificationVariable name="movingDown" id="ComponentID1VariableID10">
					<SpecificationVariableAttribute name="definition">Sa1_move_down</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)moving down(...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="11" offset="62" name="reference">InformalRequirement::REQ_PW_1_2</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="11" offset="52" name="reference">InformalRequirement::REQ_PW_4_1</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
				<SpecificationVariable name="obstacleIsDetected" id="ComponentID1VariableID11">
					<SpecificationVariableAttribute name="definition">Sa1_obstacle_detection</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)obstacle is detected(...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="20" offset="6" name="reference">InformalRequirement::REQ_PW_4_1</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
				<SpecificationVariable name="10Ms" id="ComponentID1VariableID12">
					<SpecificationVariableAttribute name="definition">10</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="description">(...)10(...)</SpecificationVariableAttribute>
					<SpecificationVariableAttribute length="2" offset="77" name="reference">InformalRequirement::REQ_PW_4_1</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeContext">no</SpecificationVariableAttribute>
					<SpecificationVariableAttribute name="timeUnit" />
				</SpecificationVariable>
			</SpecificationVariableGroup>
			<SpecificationVariableGroup name="constant" />
		</SpecificationVariableGroups>
	</Universe>
	<Assumptions>
		<AssumptionGroup name="assumptions" component="ComponentID1">
			<Assumption id="ComponentID1AssumptionID1" parent="">
				<InfoGroup name="informal">
					<Info name="name">EnvironmentalAssumption</Info>
					<Info name="description" />
					<Info name="reference_length" />
					<Info name="reference_offset" />
					<Info name="reference" />
				</InfoGroup>
				<FormalAssumption id="ComponentID1FormalAssumptionID1" specId="SPECID:UP:V1.0" accept_overflow="true">
					<Startup type="immediate" />
					<ActivationMode type="cyclic" />
					<GlobalScope>
						<Expression isInfinite="true" />
					</GlobalScope>
					<Trigger phaseId="1">
						<InterpretationMode type="progress" />
						<Condition>
							<Expression>1</Expression>
						</Condition>
					</Trigger>
					<Action phaseId="2">
						<InterpretationMode type="progress" />
						<Condition>
							<Expression>Sa1_obstacle_position &gt; 0.3</Expression>
						</Condition>
					</Action>
				</FormalAssumption>
			</Assumption>
		</AssumptionGroup>
	</Assumptions>
	<Specifications>
		<SpecificationGroup name="specifications" component="ComponentID1">
			<Specification id="ComponentID1SpecificationID1" parent="">
				<InfoGroup name="informal">
					<Info name="name">F_REQ_PW_4_1</Info>
					<Info name="description" />
					<Info name="reference_length">79</Info>
					<Info name="reference_offset">0</Info>
					<Info name="reference">InformalRequirement::REQ_PW_4_1</Info>
				</InfoGroup>
				<FormalSpecification id="ComponentID1FormalSpecificationID1" specId="SPECID:UP:V1.0" accept_overflow="true">
					<Startup type="immediate" />
					<ActivationMode type="cyclic" />
					<GlobalScope>
						<Expression isInfinite="true" />
					</GlobalScope>
					<Trigger phaseId="1">
						<InterpretationMode type="progress" />
						<Condition>
							<Expression>$obstacleIsDetected</Expression>
						</Condition>
					</Trigger>
					<Action phaseId="2">
						<Duration>
							<Expression isInfinite="false" unit="ms" interval="lower">0</Expression>
							<Expression isInfinite="false" unit="ms" interval="upper">$10Ms</Expression>
						</Duration>
						<InterpretationMode type="progress" />
						<Condition>
							<Expression>$movingDown</Expression>
						</Condition>
					</Action>
					<FormalAssumptions>
						<FormalAssumptionLinkGroup name="pattern" />
					</FormalAssumptions>
				</FormalSpecification>
			</Specification>
			<Specification id="ComponentID1SpecificationID2" parent="">
				<InfoGroup name="informal">
					<Info name="name">F_REQ_PW_1_1</Info>
					<Info name="description" />
					<Info name="reference_length">85</Info>
					<Info name="reference_offset">0</Info>
					<Info name="reference">InformalRequirement::REQ_PW_1_1</Info>
				</InfoGroup>
				<FormalSpecification id="ComponentID1FormalSpecificationID2" specId="SPECID:UP:V1.0" accept_overflow="true">
					<Startup type="immediate" />
					<ActivationMode type="cyclic" />
					<GlobalScope>
						<Expression isInfinite="true" />
					</GlobalScope>
					<Trigger phaseId="1">
						<InterpretationMode type="progress" />
						<Condition>
							<Expression>Sa1_driver_up</Expression>
						</Condition>
					</Trigger>
					<Action phaseId="2">
						<InterpretationMode type="progress" />
						<WaitDuration>
							<Expression isInfinite="false" unit="ms" interval="lower">0</Expression>
							<Expression isInfinite="false" unit="ms" interval="upper">50</Expression>
						</WaitDuration>
						<Condition>
							<Expression>Sa1_move_up</Expression>
						</Condition>
					</Action>
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
			<Requirement id="ComponentID1RequirementID1" parent="" uuid="InformalRequirement::REQ_PW_1_1">
				<InfoGroup name="origin">
					<Info name="externalID">InformalRequirement</Info>
					<Info name="name">REQ_PW_1_1</Info>
					<Info name="description">If the driver up switch is pressed, the window has to start moving up within 50 [ms].</Info>
					<Info name="externalURI">file:/home/ep/e/e/Requirements_PowerWindow.xlsx#InformalRequirement!A2</Info>
					<Info name="groupName">InformalRequirement</Info>
				</InfoGroup>
			</Requirement>
			<Requirement id="ComponentID1RequirementID2" parent="" uuid="InformalRequirement::REQ_PW_1_2">
				<InfoGroup name="origin">
					<Info name="externalID">InformalRequirement</Info>
					<Info name="name">REQ_PW_1_2</Info>
					<Info name="description">If the driver down switch is pressed, the window has to start moving down within 50 [ms], if the window is not at the bottom end.</Info>
					<Info name="externalURI">file:/home/ep/e/e/Requirements_PowerWindow.xlsx#InformalRequirement!A3</Info>
					<Info name="groupName">InformalRequirement</Info>
				</InfoGroup>
			</Requirement>
			<Requirement id="ComponentID1RequirementID3" parent="" uuid="InformalRequirement::REQ_PW_4_1">
				<InfoGroup name="origin">
					<Info name="externalID">InformalRequirement</Info>
					<Info name="name">REQ_PW_4_1</Info>
					<Info name="description">If an obstacle is detected, the window has to start moving down within 10 [ms].</Info>
					<Info name="externalURI">file:/home/ep/e/e/Requirements_PowerWindow.xlsx#InformalRequirement!A7</Info>
					<Info name="groupName">InformalRequirement</Info>
				</InfoGroup>
			</Requirement>
		</RequirementsGroup>
	</Requirements>
</SpecificationProfile>
