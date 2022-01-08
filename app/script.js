var Spotify = require('spotify-web-api-js');
var spotifyApi = new Spotify();

spotifyApi.setAccessToken('access_token');

function getPlaylists(categoryId) {
    let playlists = spotifyApi.getCategoryPlaylists(categoryId);

    const playlistsNamesIds = new Map();
    for (let i=0; i<playlists['playlists']['items']; i++) {
        let playlistName = playlists['playlists']['items'][i]['name'];
        let playlistId = playlists['playlists']['items'][i]['id'];
        playlistsNamesIds.set(playlistName, playlistId);
    }
    return playlistsNamesIds;
}

function getPlaylistTracks(playlistId) {
    let tracksInfo = spotifyApi.getPlaylistTracks(playlistId);
    const tracks = [];
    for (let t of tracksInfo['items']) {
        //get name of track
        let trackName = t['track']['name'];

        //get list of artist names
        let artistInfo = t['track']['artists'];
        const trackArtists = [];
        for (let a of artistInfo) {
            trackArtists.push(a);
        }

        //get track id
        let trackId = t['track']['id'];

        //add all to array
        const track = [trackName, trackArtists, trackId];
        tracks.push(track);
    }
    return tracks;
}

