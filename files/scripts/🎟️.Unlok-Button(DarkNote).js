// ==UserScript==
// @name         Unlock Button (Weaboo)
// @namespace    http://tampermonkey.net/
// @version      1.1
// @description  Klik tombol "Unlock" otomatis setelah 10 detik
// @author       weaboo
// @license      aanriski™ - ©weaboo
// @match        *://*/*
// @grant        GM_addStyle
// @run-at       document-start
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    function autoClickUnlock() {
        const btn = document.querySelector('button.btn.btn-primary.w-md');
        if (btn) {
            console.log('Tombol Unlock ditemukan! Menunggu 10 detik...');
            setTimeout(() => {
                console.log('Klik tombol Unlock sekarang!');
                btn.click();
            }, 10000); // 10000 ms = 10 detik
        } else {
            console.log('Tombol belum ditemukan, mencoba lagi...');
            setTimeout(autoClickUnlock, 1000); // ulang cek setiap 1 detik
        }
    }

    window.addEventListener('load', autoClickUnlock);
})();