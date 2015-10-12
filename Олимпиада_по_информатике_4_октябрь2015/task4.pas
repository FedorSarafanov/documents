const
	l = 4;
var
	a: array[1..l] of array[1..l] of char;
	t:string;
	inp,out:text;
	i,j:integer;
begin
	assign(inp,'task4.in');	assign(out,'task4.out');reset(inp);	rewrite(out);
	for i := 1 to l do begin readln(inp, t); for j := 1 to l do begin a[i][j]:=t[j]; end; end;
	// ***************************************************************************************** //
	writeln(a[1][4]);
	// ***************************************************************************************** //
	close(out);	close(inp);
end.