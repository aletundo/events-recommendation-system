@extends('layout')
@section('container')
  <div class="section" id="results">
  </div>
  <br><br>
@endsection
@section('scripts')
  <script>
  $(document).ready(function(){
    $('.sidenav').sidenav();
  });
  </script>
@endsection
