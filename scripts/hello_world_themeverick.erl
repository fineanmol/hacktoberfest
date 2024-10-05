% LANGUAGE: Erlang
% ENV: Erlang/Beam
% AUTHOR: Lamtei Wahlang
% GITHUB: https://github.com/themaverik

- module(hello_world).
- export([hello_world/0]).

-define(MSG, <<"Hello World">>).
-define(AUTHOR, <<"Lamtei">>).
-define(KHASI_TRANS, <<"Khublei Shibun!">>). %% Thank you


% prints string to standard output
hello_world() ->
    Out = <<?MSG/binary, <<" by ">>/binary, ?AUTHOR/binary, <<". ">>/binary, ?KHASI_TRANS/binary>>,
    io:format("~p~n", [binary_to_list(Out)]).