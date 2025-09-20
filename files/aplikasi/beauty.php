<?php

system("clear");
sleep(1);

function progress($message, $timeLimit, $delay) {
       for ($i = 0; $i <= $timeLimit; $i++) {
            $percent = round(($i / $timeLimit) * 100);
            $progressBar = str_repeat('▬', $i) . str_repeat(' ', $timeLimit - $i);
            echo "\r$message" . " [$progressBar] " . "$percent%\r";
            usleep($delay);
        }
        echo str_repeat(' ', 50)."\r";
    }
    
echo "PASTE KODE LALU TEKAN CTRL+D:\n\n";

// Ambil semua input dari STDIN
$log = stream_get_contents(STDIN);

progress("Processing", 30, 60000);
sleep(1);
system("clear");

// Cari JSON dalam log dan rapikan
$formattedLog = preg_replace_callback('/\{.*\}/s', function($matches) {
    $json = $matches[0];
    $data = json_decode($json, true);

    if ($data === null) {
        return $json; // Kalau error decode, balikin apa adanya
    }

    // JSON sudah rapi
    $pretty = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);

    // Prefix setiap baris dengan "║  "
    $lines = explode("\n", $pretty);
    $prefixed = "";
    foreach ($lines as $line) {
        $prefixed .= "║  " . $line . "\n";
    }

    // Hapus newline terakhir biar nggak ngusir garis bawah
    return rtrim($prefixed, "\n");
}, $log);

// Tampilkan hasil
echo "\n=== HASIL KODE YANG DI RAPIKAN ===\n\n";
echo $formattedLog;


// Simpan ke memori internal (sdcard)
$outputFile = "/sdcard/beauty.log";
if (@file_put_contents($outputFile, $formattedLog)) {
    echo "\n\n✔ Hasil disimpan ke: $outputFile\n";
} else {
    echo "\n\n✘ Gagal menyimpan ke: $outputFile\n";
    echo "Coba kasih izin Termux:  termux-setup-storage\n";
}
