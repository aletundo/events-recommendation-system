@extends('layout')
@section('container')
  <div class="section">
    <h1 class="header center orange-text">Our recommendations</h1>
  </div>
  <div class="section" id="results">
    <div class="row">
      <div class="col s3">
        <h5 class="light-blue-text">Similar users</h5>
        <ul class="collection">
        @foreach ($users as $user)
          <li class="collection-item avatar">
            <img src="{{ $user->avatar }}" alt="" class="circle">
            <span class="title event-title">{{ $user->firstname }} {{ $user->lastname }}</span>
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
      <div class="col s9">
        <div class="row">
          <h5 class="light-blue-text">Events</h5>
        </div>
        <div class="row center vertical-align">
          <form action="{{ url()->full() }}" method="get">
            <input type="hidden" name="user" value="{{ request()->user }}">
            <div class="col s5">
              <div class="input-field">
                <select multiple name="categories[]">
                  <option value="Arte" @if (in_array('Arte', request()->categories)) selected @endif>Arte</option>
                  <option value="Cibo" @if (in_array('Cibo',request()->categories)) selected @endif>Cibo</option>
                  <option value="Festa" @if (in_array('Festa',request()->categories)) selected @endif>Festa</option>
                  <option value="Musica" @if (in_array('Musica',request()->categories)) selected @endif>Musica</option>
                  <option value="Sport" @if (in_array('Sport',request()->categories)) selected @endif>Sport</option>
                </select>
                <label>Categories</label>
              </div>
            </div>
            <div class="col s3">
              <label>Sort by category</label>
                 <div class="switch"><label>Off<input type="checkbox" name="sort" @isset(request()->sort))
                   checked
                 @endisset>
                    <span class="lever"></span>On</label></div>
            </div>
            <div class="col s4">
              <button class="btn waves-effect waves-light orange" type="submit" name="action">Refresh
                <i class="material-icons right">refresh</i>
              </button>
            </div>
            {{-- <div class="col s6">
              {{ $events->appends([
                'user' => request()->user,
                'categories' => request()->categories,
                'features' => request()->features,
                ])->links() }}
            </div>
            <div class="col s3">
              <label>Sort by category</label>
                 <div class="switch"><label>Off<input type="checkbox">
                    <span class="lever"></span>On</label></div>
            </div> --}}
          </form>
        </div>
        @php
          $elements_counter = 0;
        @endphp
        @foreach ($events as $event)
          @if($elements_counter === 0)
          <div class="row events">
          @endif
            <div class="col s4 event-column">
              <div class="card sticky-action event">
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
          {{ $events->appends([
            'user' => request()->user,
            'categories' => request()->categories,
            'features' => request()->features,
            'sort' => request()->sort,
            ])->links() }}
        </div>
      </div>
    </div>
  </div>
  <br><br>
@endsection
@section('scripts')
  @parent
  <script>
  $(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').select();
  });
  </script>
@endsection
