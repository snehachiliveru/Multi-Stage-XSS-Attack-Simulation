<?php
// cookie_hardening.php - set secure cookie params (example)
// Note: 'secure' requires HTTPS in production
session_set_cookie_params([
    'lifetime' => 0,
    'path' => '/',
    'domain' => '', 
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Strict'
]);
session_start();
echo "Session cookie set with HttpOnly, Secure, SameSite=Strict (example)";
?>