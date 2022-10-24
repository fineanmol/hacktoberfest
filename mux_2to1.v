module m21(Y, D0, D1, S);

output Y;
input D0, D1, S;
wire T1, T2, Sbar;

and (T1, D1, S), (T2, D0, Sbar);
not (Sbar, S);
or (Y, T1, T2);

endmodule
