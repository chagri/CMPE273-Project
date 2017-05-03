 
   
   <?php
$pageTitle = "INSERT USER";
include("inc/header.php"); ?>

 
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
       "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

    <!-- Fig. 26.19: database.php        -->
    <!-- Program to query a database and -->
    <!-- send results to the client.     -->

    <html xmlns = "http://www.w3.org/1999/xhtml">
       <head>
         <title>Search Results</title>
      </head>

      <body style = "font-family: arial, sans-serif"
         style = "background-color: #F0E68C">
         <?php

            extract( $_POST );
                        
            $sql = "INSERT INTO greensheet (subject_code, subject_name, section_name,section_period,instructor,office_location,email,office_hours,class_days
            ,classroom,prerequisites,canvas_website,course_description,textbooks_and_materials,canvas_format,classroom_protocol,course_requirements,drop_and_add,general_rules) VALUES ('$_POST[subject_code]',
             '$_POST[subject_name]',    '$_POST[section_name]','$_POST[section_period]','$_POST[instructor]','$_POST[office_location]','$_POST[txtcomment]','$_POST[office_hours]',
            '$_POST[class_days]',
            '$_POST[classroom]',
            '$_POST[prerequisites]','$_POST[canvas_website]','$_POST[course_description]','$_POST[textbooks_and_materials]','$_POST[canvas_format]','$_POST[classroom_protocol]',
            '$_POST[course_requirements]','$_POST[drop_and_add]','$_POST[general_rules]')";
            
            
            // Connect to MySQL
            if ( !( $database = mysql_connect( "localhost","thebarca_1", "Leomessi@123" ) ) )
            {
               die( "Could not connect to a database" );
            }
            
            // open Products database
            
            if ( !(mysql_select_db('thebarca_storedata', $database) ))
            {
               die( "Could not open Products database" );
            }

            // query Products database
            if ( !( $result = mysql_query( $sql, $database ) ) ) 
             {
               print( "Could not execute query!<br/><br/>");
               print( "Greensheet already exists<br/><br/>");
               die( mysql_error() );
            }
            else{
            print ("<h1>successfully inserted</h1>");
            }
                   ?>

      </body>
   </html>
   
<?php include("inc/footer.php"); ?>
