<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $website = htmlspecialchars($_POST['site']);
    $comment = htmlspecialchars($_POST['comment']);

    echo "<h2>Form Submission Successful!</h2>";
    echo "Thank you, " . $name . ". I have received your email: " . $email;
    echo "Your website is" . $website . "And your comments" . $comment . "were received";
    
} else {
    header("Location: contact.html");
    exit();
}
?>