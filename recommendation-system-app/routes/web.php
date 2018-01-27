<?php
use Illuminate\Http\Request;
use GuzzleHttp\Exception\GuzzleException;
use GuzzleHttp\Client;

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
    $response = $client->get('users/' . $request->user . '/recommendations');
    return $response->getBody();
})->name('events');
