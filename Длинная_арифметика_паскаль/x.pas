uses SysUtils;

var
	i,j,d,k,m: Integer;
	a,b,c: String;

function Revert(S: string):string;
var
 i: byte;
 T: string;
begin
 T:='';
 for i:=length(S) downto 1 do
  T:=T+S[i];
 Revert:=T;
end;

begin
	c:='000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000';
	d:=0;
	k:=0;
	readln(a);
	readln(b);
	for i := Length(a) downto 1 do
	begin
		inc(d);
		for j := Length(b) downto 1 do
		begin
			if k=Length(b) then k:=0;
			inc(k);	
			writeln(k);			
			writeln(k,' ',d);
			c[k+d-1]:=IntToStr(((StrToInt(a[i])*StrToInt(b[j])) mod 10)+StrToInt(c[k+d-1]))[1];
			c[k+d]:=IntToStr(((StrToInt(a[i])*StrToInt(b[j])) div 10)+StrToInt(c[k+d]))[1];
			m:=k+d;
		end;
	end;
	c:=Copy(c,1,m);
	c:=Revert(c);
	if c[0]='0' then c:=Copy(c,2,m);
	writeln(c);
end.