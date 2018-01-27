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
    <div class="nav-wrapper container"><a id="logo-container" href="{{ route('welcome') }}" class="brand-logo">rEvent</a>
      <ul class="right hide-on-med-and-down">
        <li><a href="{{ route('welcome') }}">Get events</a></li>
        <li><a href="#about">About</a></li>
      </ul>

      <ul id="nav-mobile" class="sidenav">
        <li><a href="{{ route('welcome') }}">Get events</a></li>
        <li><a href="#about">About</a></li>
      </ul>
      <a href="#" data-target="nav-mobile" class="sidenav-trigger"><i class="material-icons">menu</i></a>
    </div>
  </nav>
  @yield('intro')

  <div class="container">
    @yield('container')
  </div>

  <footer class="page-footer orange" id="about">
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
  @yield('scripts')
</body>
</html>
