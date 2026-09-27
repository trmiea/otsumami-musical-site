const fs = require('fs');

const dataStr = fs.readFileSync('res/input/archive.json', 'utf8');
try {
    const data = JSON.parse(dataStr);
    const html = data.map(vol => `
        <div class="archive-card">
            <div class="archive-header">
                <h2 class="archive-title">${vol.title}</h2>
                <div class="archive-date">${vol.date}</div>
            </div>
            <div class="archive-content">
                <div>
                    <h3 style="text-align: left; font-size: 1.1rem; margin-top: 0;">Setlist (${vol.songs.length} songs)</h3>
                    <ul class="song-list">
                        ${vol.songs.map(song => `
                            <li class="song-item">
                                ${song.youtube_url ? `<a href="${song.youtube_url}" target="_blank" class="song-item-content">` : `<div class="song-item-content">`}
                                    <span class="song-title">${song.title}${song.youtube_url ? ' <span style="font-size:0.8rem; color:#c29a5b; margin-left:5px;">▶︎</span>' : ''}</span>
                                    <span class="song-work">${song.work}</span>
                                ${song.youtube_url ? `</a>` : `</div>`}
                            </li>
                        `).join('')}
                    </ul>
                </div>
                <div class="links-area">
                    <h3 style="margin-top: 0; font-size: 1.1rem;">Gallery & Media</h3>
                    <p style="font-size: 0.85rem; color: #888;">本番の写真や動画などをGoogle Driveで公開しています。</p>
                    <div style="display: flex; gap: 10px; margin-top: 15px;">
                        <a href="${vol.photo_url}" target="_blank" class="btn-gold-outline" style="margin-top: 0; text-align: center; flex: 1;">Photos ↗</a>
                        <a href="${vol.video_url}" target="_blank" class="btn-gold-outline" style="margin-top: 0; text-align: center; flex: 1;">Videos ↗</a>
                    </div>
                </div>
            </div>
        </div>
    `).join('');
    console.log("SUCCESS length:", html.length);
} catch(e) {
    console.error("ERROR:", e);
}
