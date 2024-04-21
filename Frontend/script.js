document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const mediaType = urlParams.get('media_type');
    const itemId = urlParams.get('id');

    if (mediaType === 'movie' && itemId) {
        obtenerDetalles('movie', itemId);
    } else if (mediaType === 'tv' && itemId) {
        obtenerDetalles('tv', itemId);
    } else {
        obtenerMedios('movie');
        obtenerMedios('tv');
    }
});

function obtenerMedios(mediaType) {
    fetch(`https://api.themoviedb.org/3/discover/${mediaType}?api_key=fe1a6340812a4559051b8ec620a4e866&language=es&sort_by=popularity.desc&page=1`)
        .then(response => response.json())
        .then(data => mostrarMedios(data.results, mediaType))
        .catch(error => console.error(`Error al obtener ${mediaType}s:`, error));
}

function mostrarMedios(medios, mediaType) {
    const mediaRow = document.getElementById(`${mediaType}sRow`);

    medios.forEach(medio => {
        const mediaListItem = document.createElement('a');
        mediaListItem.classList.add('col-md-3', 'media-list-item');
        mediaListItem.href = `detalleMedia.html?media_type=${mediaType}&id=${medio.id}`;

        const image = document.createElement('img');
        image.src = `https://image.tmdb.org/t/p/w500${medio.poster_path}`;
        image.classList.add('media-image');
        mediaListItem.appendChild(image);

        const title = document.createElement('h2');
        title.textContent = mediaType === 'movie' ? medio.title : medio.name;
        title.classList.add('media-title');
        mediaListItem.appendChild(title);

        mediaRow.appendChild(mediaListItem);
    });
}

function obtenerDetalles(mediaType, id) {
    fetch(`https://api.themoviedb.org/3/${mediaType}/${id}?api_key=fe1a6340812a4559051b8ec620a4e866&language=es`)
        .then(response => response.json())
        .then(data => {
            mostrarDetalles(data, mediaType);
            obtenerTrailer(mediaType, id);
        })
        .catch(error => console.error(`Error al obtener detalles de ${mediaType}:`, error));
}

function mostrarDetalles(media, mediaType) {
    const mediaImage = document.getElementById('mediaImage');
    const mediaTitle = document.getElementById('mediaTitle');
    const mediaOverview = document.getElementById('mediaOverview');

    mediaImage.src = `https://image.tmdb.org/t/p/w500${media.poster_path}`;
    mediaTitle.textContent = mediaType === 'movie' ? media.title : media.name;
    mediaOverview.textContent = media.overview;
}

function obtenerTrailer(mediaType, id) {
    fetch(`https://api.themoviedb.org/3/${mediaType}/${id}/videos?api_key=fe1a6340812a4559051b8ec620a4e866&language=es`)
        .then(response => response.json())
        .then(data => {
            if (data.results.length > 0) {
                const trailerKey = data.results[0].key;
                mostrarTrailer(trailerKey);
            } else {
                console.error(`No se encontraron trailers para este ${mediaType}`);
            }
        })
        .catch(error => console.error(`Error al obtener el trailer de ${mediaType}:`, error));
}

function mostrarTrailer(key) {
    const youtubeVideo = document.getElementById('youtubeVideo');
    youtubeVideo.innerHTML = `
        <iframe
            width="100%"
            height="400"
            src="https://www.youtube.com/embed/${key}"
            title="YouTube video player"
            frameborder="0"
            allowfullscreen
        ></iframe>
    `;
}
