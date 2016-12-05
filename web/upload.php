<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$fileType = pathinfo($target_file,PATHINFO_EXTENSION);

if(isset($_POST["submit"])) {
    if($fileType != "txt") {
        echo "<script> upload_error(); </script>";
        $uploadOk = 1;
    } else {
        echo "Done!";
        $uploadOk = 1;
    }
}
?>