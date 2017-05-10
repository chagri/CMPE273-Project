<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>GREENSHEET</title>
<link rel="stylesheet" type="text/css" href="view.css" media="all">
<script type="text/javascript" src="view.js"></script>
<script type="text/javascript" src="calendar.js"></script>
</head>

<body id="main_body" >
	
	<img id="top" src="top.png" alt="">
	<div id="form_container">
	
		<h1><a>GREENSHEET</a></h1>
		<form id="form_29247" class="appnitro"  method="post" action="createGreensheet.php">
					<div class="form_description">
			<h2>GREENSHEET</h2>
			<p></p>
		</div>						
			<ul >
			
					<li class="section_break">
			<h3>Information</h3>
			<p></p>
		</li>		<li id="li_1" >
		<label class="description" for="element_1">Subject Code </label>
		<div>
			<input id="element_1" name="subject_code" class="element text large" type="text" maxlength="255" value=""/> 
		</div><p class="guidelines" id="guide_1"><small>Please enter subject code. For example: 202</small></p> 
		</li>		<li id="li_2" >
		<label class="description" for="element_2">Subject Name </label>
		<div>
			<input id="element_2" name="subject_name" class="element text large" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_3" >
		<label class="description" for="element_3">Section Number </label>
		<div>
			<input id="element_3" name="section_name" class="element text large" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_19" >
		<label class="description" for="element_19">Period/Year </label>
		<div>
		<select class="element select large" id="element_19" name="element_19"> 
			<option value="<?php echo $data2[section_period];?>" selected="selected"></option>
                        <option value="1" >Spring 2017</option>
                        <option value="2" >Fall 2018</option>
                        <option value="3" >Spring 2018</option>
		</select>
		</div> 
		</li>		<li id="li_4" >
		<label class="description" for="element_4">Instructor </label>
		<div>
			<input id="element_4" name="instructor" class="element text large" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_5" >
		<label class="description" for="element_5">Office location </label>
		<div>
			<input id="element_5" name="office_location" class="element text large" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_6" >
		<label class="description" for="element_6">Email </label>
		<div>
			<input id="element_6" name="email" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_7" >
		<label class="description" for="element_7">Office hours </label>
		<div>
			<input id="element_7" name="office_hours" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_8" >
		<label class="description" for="element_8">Class Days/Time </label>
		<div>
			<input id="element_8" name="class_days" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_9" >
		<label class="description" for="element_9">Classroom </label>
		<div>
			<input id="element_9" name="classroom" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_10" >
		<label class="description" for="element_10">Prerequisite </label>
		<div>
			<textarea id="element_10" name="prerequisites" class="element textarea medium"></textarea> 
		</div> 
		</li>		<li id="li_11" >
		<label class="description" for="element_11">Course Website </label>
		<div>
			<input id="element_11" name="canvas_website" class="element text large" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_12" >
		<label class="description" for="element_12">Course description </label>
		<div>
			<textarea id="element_12" name="course_description" class="element textarea large"></textarea> 
		</div> 
		</li>		<li id="li_13" >
		<label class="description" for="element_13">Textbook and Material </label>
		<div>
			<textarea id="element_13" name="textbooks_and_materials" class="element textarea large"></textarea> 
		</div> 
		</li>		<li id="li_14" >
		<label class="description" for="element_14">Canvas Format </label>
		<div>
			<input id="element_14" name="canvas_format" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_15" >
		<label class="description" for="element_15">Classroom Protocols </label>
		<div>
			<textarea id="element_15" name="classroom_protocol" class="element textarea large"></textarea> 
		</div> 
		</li>		<li id="li_16" >
		<label class="description" for="element_16">Course requirements </label>
		<div>
			<textarea id="element_16" name="course_requirements" class="element textarea medium"></textarea> 
		</div> 
		</li>		<li id="li_17" >
		<label class="description" for="element_17">General Rule </label>
		<div>
			<textarea id="element_17" name="general_rules" class="element textarea large"></textarea> 
		</div> 
		</li>		<li id="li_18" >
		<label class="description" for="element_18">Drop and Add  </label>
		<div>
			<textarea id="element_18" name="drop_and_add" class="element textarea medium"></textarea> 
		</div> 
		</li>		<li class="section_break">
			<h3>Grading Policies</h3>
			<p></p>
		</li>		<li id="li_21" >
		<label class="description" for="element_21">Labs </label>
		<div>
			<input id="element_21" name="labs" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_22" >
		<label class="description" for="element_22">Quiz </label>
		<div>
			<input id="element_22" name="quizzes" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_23" >
		<label class="description" for="element_23">Assignment </label>
		<div>
			<input id="element_23" name="assignments" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_24" >
		<label class="description" for="element_24">Project </label>
		<div>
			<input id="element_24" name="project" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_25" >
		<label class="description" for="element_25">Mid Term </label>
		<div>
			<input id="element_25" name="mid_term" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_26" >
		<label class="description" for="element_26">Final Term </label>
		<div>
			<input id="element_26" name="final_term" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_27" >
		<label class="description" for="element_27">Grading Pattern </label>
		<div>
			<input id="element_27" name="grading_pattern" class="element text medium" type="text" maxlength="255"
			 value="<?php echo $data3[grading_pattern];?>"/> 
		</div> 
		</li>		<li class="section_break">
			<h3>Course Schedule</h3>
			<p></p>
		</li>		<li id="li_29" >
		
		<label class="description" for="element_29">Date </label>
		<div>
			<input id="element_29" name="element_29" class="element text large" type="text" maxlength="255" value=""/> 
		</div> 
		</li>
		
		<li id="li_30" >
		<label class="description" for="element_30">Topic </label>
		<div>
			<input id="element_30" name="element_30" class="element text large" type="text" maxlength="255" value=""/> 
		</div> 
		</li>		<li id="li_31" >
		<label class="description" for="element_31">Dues </label>
		<div>
			<input id="element_31" name="element_31" class="element text medium" type="text" maxlength="255" value=""/> 
		</div> 
		</li>
					<li class="buttons">
			    <input type="hidden" name="form_id" value="29247" />
			    
				<input id="updateForm" class="button_text" type="submit" name="submit" value="CREATE" />
		</li>
			</ul>
		</form>	
		<div id="footer">
			<p>San Jose State University</P>
		</div>
	</div>
	<img id="bottom" src="bottom.png" alt="">
	</body>

</html>