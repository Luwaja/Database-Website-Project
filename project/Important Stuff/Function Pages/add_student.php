<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Add Student</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="function.css">
    </head>
    <body style="background-color: rgb(75, 75, 75);">
        <button onclick="goBack()">Go Back</button>
        <h1 class="center white">Add Student</h1>
        
        <form class="center white" action="add_student.php" method="post">
            Name: <br><br>
            <input type="text" name="name">
            <br><br>
            Major: <br><br>
            <input type="text" name="major">
            <br><br>
            <input name="submit" type="submit" >
        </form>
        <p class="center white" >Submitted!</p>

    </body>

    <script>
        function goBack()
        {
            window.history.back();
        }
    </script>
</html>

<?php
if (isset($_POST['submit'])) 
{
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
    // add ' ' around multiple strings so they are treated as single command line args
    $name = escapeshellarg($_POST['name']);
    $major = escapeshellarg($_POST['major']);

    // build the linux command that you want executed;  
    $command = 'python add_student.py ' . $name . ' ' . $major;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    echo "$name";
    echo "$major";
    system($command);           
}
?>
