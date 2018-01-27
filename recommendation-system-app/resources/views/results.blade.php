@extends('layout')
@section('container')
  <div class="section">
    <h1 class="header center orange-text">Our recommendations</h1>
  </div>
  <div class="section" id="results">
    <div class="row">
      <div class="col s2">
        <h5 class="light-blue-text">Similar users</h5>
        <ul class="collection">
        @foreach ($users as $user)
          <li class="collection-item avatar">
            <img src="{{ $user->avatar }}" alt="" class="circle">
            <span class="title">{{ $user->firstname }} {{ $user->lastname }}</span>
            <p>
              <span><i class="material-icons">location_city</i>&nbsp;{{ $user->city }}</span>
              <br>
              <span><i class="material-icons">wc</i>&nbsp;{{ $user->gender }}</span>
              <br>
              <span><i class="material-icons">cake</i>&nbsp;{{ $user->age }}</span>
            </p>
          </li>
        @endforeach
        </ul>
      </div>
      <div class="col s10">
        <h5 class="light-blue-text">Events</h5>
        <div class="row center">
          {{ $events->appends(['user' => request()->user])->links() }}
        </div>
        @php
          $elements_counter = 0;
        @endphp
        @foreach ($events as $event)
          @if($elements_counter === 0)
          <div class="row">
          @endif
            <div class="col s4">
              <div class="card sticky-action">
                <div class="card-image waves-effect waves-block waves-light">
                  <img class="activator" src="{{ $event->picture->data->url }}">
                </div>
                <div class="card-content">
                  <span class="card-title activator grey-text text-darken-4">{{ $event->name }}<i class="material-icons right">more_vert</i></span>
                  <p>
                    <span><i class="material-icons">place</i>&nbsp;{{ $event->place .' ('. $event->city . ')'}}</span>
                    <br>
                    <span><i class="material-icons">style</i>&nbsp;{{ $event->category }}</span>
                  </p>
                </div>
                <div class="card-reveal">
                  <span class="card-title grey-text text-darken-4">{{ $event->name }}<i class="material-icons right">close</i></span>
                  <p>
                    @php
                      if(isset($event->description))
                        echo nl2br($event->description)
                    @endphp
                  </p>
                </div>
                <div class="card-action">
                  <a href="https://facebook.com/events/{{ $event->id }}">Check it on Facebook!</a>
                </div>
              </div>
            </div>
          @if($elements_counter === 2 || $loop->last)
          </div>
          @endif
          @php
            if($elements_counter === 2)
              $elements_counter = 0;
            else
              $elements_counter++;
          @endphp
        @endforeach
        <div class="row center">
          {{ $events->appends(['user' => request()->user])->links() }}
        </div>
      </div>
    </div>
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
