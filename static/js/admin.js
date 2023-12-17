document.addEventListener("DOMContentLoaded", function () {
  var Button = null;
  function playSong() {
    paused = !paused;
    if (Button != this && !$(this).is($(".play-btn"))) {
      $(".song-button").html('<i class="bi bi-play"></i>');
      $(".play-btn").html('<i class="bi bi-pause-fill"></i>');
      const song = JSON.parse($(this).attr("data-attr"));
      $(".song-title-bottom").html(song.name);
      $(".song-artist-bottom").html(song.artist);
      if ($(".player-bottom").attr("src") != song.song) {
        $(".audio-wrapper").html(
          `<audio id="player" autoplay>
                <source class="player-bottom" src=${song.song}  type="audio/mp3">
              </audio>`
        );
      }
      $(".album-image").css("background-image", `url(${song.image})`);
      Button = this;

      document
        .getElementById("player")
        .addEventListener("timeupdate", initProgressBar);

      document
        .getElementById("player")
        .addEventListener("loadeddata", initProgressBar);
      function initProgressBar() {
        var player = document.getElementById("player");
        var length = player.duration;
        var current_time = player.currentTime;

        // calculate total length of value
        var totalLength = calculateTotalValue(length);
        document.getElementById("end-time").innerHTML = totalLength;

        // calculate current value time
        var currentTime = calculateCurrentValue(current_time);
        document.getElementById("start-time").innerHTML = currentTime;

        var progressbar = document.getElementById("seek-obj");
        progressbar.value = player.currentTime / player.duration;
        progressbar.addEventListener("click", seek);

        function seek(event) {
          var percent = event.offsetX / this.offsetWidth;
          player.currentTime = percent * player.duration;
          progressbar.value = percent / 100;
        }
      }

      function initPlayers(num) {
        // pass num in if there are multiple audio players e.g 'player' + i

        for (var i = 0; i < num; i++) {
          (function () {
            (player = document.getElementById("player")),
              (isPlaying = false),
              function togglePlay() {
                if (player.paused === false) {
                  player.pause();
                  isPlaying = false;
                  $(Button).html('<i class="bi bi-play"></i>');
                } else {
                  player.play();
                  isPlaying = true;
                  $(Button).html('<i class="bi bi-pause"></i>');
                }
              };
          })();
        }
      }

      function calculateTotalValue(length) {
        let ismorethanhour =
          new Date(length * 1000).toISOString().substr(11, 2) > 0;
        let time = ismorethanhour
          ? new Date(length * 1000).toISOString().substr(11, 8)
          : new Date(length * 1000).toISOString().substr(14, 5);
        return time;
      }

      function calculateCurrentValue(length) {
        let ismorethanhour =
          new Date(length * 1000).toISOString().substr(11, 2) > 0;
        let time = ismorethanhour
          ? new Date(length * 1000).toISOString().substr(11, 8)
          : new Date(length * 1000).toISOString().substr(14, 5);

        return time;
      }

      initPlayers(jQuery("#player-container").length);
    }

    if (!paused) $("#player").trigger("pause");
    else $("#player").trigger("play");
    if (paused) {
      $(Button).html('<i class="bi bi-pause"></i>');
      $(".play-btn").html('<i class="bi bi-pause-fill"></i>');
      console.log("paused");
    } else {
      $(Button).html('<i class="bi bi-play"></i>');
      $(".play-btn").html('<i class="bi bi-play-fill"></i>');
    }
  }
  var paused = false;

  $(".song-button").on("click", playSong);
  $(".play-btn").on("click", playSong);
});
