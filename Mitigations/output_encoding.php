<?php
// output_encoding.php - example to demonstrate htmlspecialchars output escaping
$user_input = $_GET['input'] ?? '';
// Before (vulnerable): echo $user_input;
// After (safe):
echo htmlspecialchars($user_input, ENT_QUOTES | ENT_HTML5, 'UTF-8');
?>