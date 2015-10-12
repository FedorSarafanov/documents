var
	pon,srd,cht: integer;
	hour: integer;
	hours: integer;
	i,j:integer;
begin
	readln(hour);

	while hours<>hour do
	begin
		inc(i);
		if i=1 then
		begin
			inc(pon);
			hours:=hours+2;
			if hours=hour then writeln('ponedelnik',pon);
		end;
		if i=2 then
		begin
			inc(srd);
			hours:=hours+2;
			if hours=hour then writeln('sreda',srd);
		end;
		if i=3 then
		begin
			inc(cht);
			hours:=hours+1;
			if hours=hour then writeln('chetverg',cht);
		end;						
	end;
	
end.