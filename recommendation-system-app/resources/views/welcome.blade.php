<!DOCTYPE html>
<html lang="{{ app()->getLocale() }}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">

  <title>{{ config("app.name") }}</title>
  <!-- Compiled and minified CSS -->
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-alpha.2/css/materialize.min.css">
  <link href="https://use.fontawesome.com/releases/v5.0.0/css/all.css" rel="stylesheet">
  <link href="css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
</head>
<body>
  <nav class="light-blue lighten-1" role="navigation">
    <div class="nav-wrapper container"><a id="logo-container" href="#" class="brand-logo">rEvent</a>
      <ul class="right hide-on-med-and-down">
        <li><a href="#getEvents">Get events</a></li>
        <li><a href="#">About</a></li>
      </ul>

      <ul id="nav-mobile" class="sidenav">
        <li><a href="#getEvents">Get events</a></li>
        <li><a href="#">About</a></li>
      </ul>
      <a href="#" data-target="nav-mobile" class="sidenav-trigger"><i class="material-icons">menu</i></a>
    </div>
  </nav>
  <div class="section no-pad-bot" id="index-banner">
    <div class="container">
      <br><br>
      <h1 class="header center orange-text">rEvent</h1>
      <div class="row center">
        <h5 class="header col s12 light">A Facebook events recommendation system</h5>
      </div>
      <div class="row center">
        <a href="#getEvents" id="call-to-action-button" class="btn-large waves-effect waves-light orange">Let's go!</a>
      </div>
      <br><br>

    </div>
  </div>

  <div class="container">
    <div class="section">

      <!--   Icon Section   -->
      <div class="row">
        <div class="col s12 m4">
          <div class="icon-block">
            <h2 class="center light-blue-text"><i class="material-icons">flash_on</i></h2>
            <h5 class="center">Fast results</h5>

            <p class="light">Get events in two shakes! Thanks to our powerful systems we provide results x150 faster than any other competitor.</p>
          </div>
        </div>

        <div class="col s12 m4">
          <div class="icon-block">
            <h2 class="center light-blue-text"><i class="material-icons">face</i></h2>
            <h5 class="center">User centered</h5>

            <p class="light">By using users interests and categorization we provide high targeted results.</p>
          </div>
        </div>

        <div class="col s12 m4">
          <div class="icon-block">
            <h2 class="center light-blue-text"><i class="material-icons">highlight</i></h2>
            <h5 class="center">Easy to work with</h5>

            <p class="light">Set your filters and you are ready to go. We care about the black magic for you :)</p>
          </div>
        </div>
      </div>

    </div>
    <div class="section" id="getEvents">
      <h2 class="header orange-text">Get events</h1>
      <div class="row">
        <form class="col s12" action="{{ route('api.events.retrieve') }}" method="get">
          {{ csrf_field() }}
          <div class="row">
            <div class="input-field col s12 m6">
              <select multiple class="icons" name="users[]">
                <option value="" disabled>Choose users</option>
                <option value="1" data-icon="https://tinyfac.es/data/avatars/FBEBF655-4886-455A-A4A4-D62B77DD419B-200w.jpeg">Mario Rossi</option>
                <option value="2" data-icon="https://tinyfac.es/data/avatars/A7299C8E-CEFC-47D9-939A-3C8CA0EA4D13-200w.jpeg">Rebecca Fulz</option>
                <option value="3" data-icon="https://tinyfac.es/data/avatars/2DDDE973-40EC-4004-ABC0-73FD4CD6D042-200w.jpeg">Francesco Milo</option>
              </select>
              <label>Users</label>
            </div>

            <div class="input-field col s12 m6">
              <select multiple name="categories[]">
                <option value="" disabled>Choose categories</option>
                <optgroup label="Sport">
                  <option value="calcio">Soccer</option>
                  <option value="basket">Basket</option>
                </optgroup>
                <optgroup label="Food">
                  <option value="pizza">Pizza</option>
                  <option value="vegetariano">Veg</option>
                </optgroup>
              </select>
              <label>Categories</label>
            </div>
          </div>

          <div class="row center">
            <button class="btn waves-effect waves-light" type="submit" name="action">Inspire me
              <i class="material-icons right">wb_incandescent</i>
            </button>
          </div>
        </form>
      </div>
    </div>
    <br><br>
  </div>

  <footer class="page-footer orange">
    <div class="container">
      <div class="row">
        <div class="col l6 s12">
          <h5 class="white-text">Team</h5>
          <ul>
            <li><a class="white-text" href="https://github.com/aletundo" target="_blank"><i class="fas fa-hand-peace"></i>&nbsp;Alessandro Tundo</a></li>
            <li><a class="white-text" href="https://github.com/oet93" target="_blank"><i class="fas fa-hand-spock"></i>&nbsp;Matteo Vaghi</a></li>
          </ul>
        </div>
        <div class="col l6 s12">
          <h5 class="white-text">Useful links</h5>
          <ul>
            <li><a class="white-text" href="https://github.com/aletundo/events-recommendation-system" target="_blank"><i class="fab fa-github"></i>&nbsp;Github project</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-copyright">
      <div class="container">
        Made by <a class="orange-text text-lighten-3" href="https://github.com/aletundo/events-recommendation-system" target="_blank">Alessandro Tundo &amp; Matteo Vaghi</a>
      </div>
    </div>
  </footer>

  <!--  Scripts-->
  <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
  <!-- Compiled and minified JavaScript -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-alpha.2/js/materialize.min.js"></script>
  <script>
  $(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').select();
    $.ajax({
  url: 'https://tinyfac.es/api/users',
  dataType: 'json',
  success: function(data) {
      console.log(data);
  }
});
  });
  </script>
</body>
</html>
