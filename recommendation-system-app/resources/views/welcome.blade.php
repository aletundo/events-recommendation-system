@extends('layout')
@section('intro')
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
@endsection
@section('container')
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
    <h2 class="header orange-text"></h1>
    <div class="row">
      <form class="col s12" action="{{ route('events') }}" method="get">
        <div class="row">
          <div class="input-field col s12 m12">
            <select class="icons" name="user">
              <option selected value="" disabled>Choose a user</option>
              @foreach ($users as $user)
                <option value="{{ $user->_id->{'$oid'} }}" data-icon="{{ $user->avatar }}">{{ $user->firstname .' '. $user->lastname }}</option>
              @endforeach
            </select>
            <label>Users</label>
          </div>
        </div>
        <div class="row center">
          <button class="btn waves-effect waves-light pulse" type="submit" name="action">Inspire me
            <i class="material-icons right">wb_incandescent</i>
          </button>
        </div>
      </form>
    </div>
  </div>
  <br><br>
@endsection
@section('scripts')
  <script>
  $(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').select();
  });
  </script>
@endsection
