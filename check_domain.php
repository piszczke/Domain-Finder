<?php
if (isset($_GET['domain'])) {
    $domain = $_GET['domain'];
    $output = shell_exec("python3 check_domain.py " . escapeshellarg($domain));
    $available = strpos($output, 'is available') !== false;
    echo json_encode(['available' => $available]);
} else {
    echo json_encode(['error' => 'No domain provided']);
}
?>