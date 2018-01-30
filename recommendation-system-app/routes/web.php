<?php
use Illuminate\Http\Request;
use GuzzleHttp\Exception\GuzzleException;
use GuzzleHttp\Client;
use Illuminate\Pagination\Paginator;
use Illuminate\Pagination\LengthAwarePaginator;
use Illuminate\Support\Collection;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    $client = new Client(['base_uri' => 'http://recommendation-system-engine:5000/']);
    $response = $client->get('users');
    $users = json_decode($response->getBody());
    return view('welcome', ['users' => $users]);
})->name('welcome');

Route::get('/events', function (Request $request) {
    $client = new Client(['base_uri' => 'http://recommendation-system-engine:5000/']);
    $response = $client->get('users/' . $request->user . '/recommendations', [
      'query' => isset($request->features) ? ['features' => $request->features ] : [],
    ]);
    $results = json_decode($response->getBody());
    $targetUser = $results->target_user;
    $users = $results->users;
    $events = collect($results->events);
    if ($request->sort) {
      $events = $events->sortBy('category');
    }
    if($request->categories) {
      $categories = $request->categories;
      $filtered = $events->filter(function ($value, $key) use ($categories) {
        if (in_array($value->category, $categories)) {
          return $value;
        }
      });
      return view('results', ['targetUser' => $targetUser, 'users' => $users, 'events' => paginateCollection($filtered, 12)]);
    }
    return view('results', ['targetUser' => $targetUser, 'users' => $users, 'events' => paginateCollection($events, 12)]);
})->name('events');

function paginateCollection(Collection $collection, int $perPage){
    $currentPage = LengthAwarePaginator::resolveCurrentPage();
    $currentPageItems = $collection->forPage($currentPage, $perPage);
    $paginator = new LengthAwarePaginator($currentPageItems, count($collection), $perPage);
    $paginator->setPath(app()->request->url());
    return $paginator;
}
