function trans(p)
fid = fopen('data4.txt','wt');
fprintf(fid,'@data');
fprintf(fid,'\n');

for i=1:672
    var u=0;
    for j=1:163949
        if p(i,j)>5
            u=1;
            fprintf(fid,int2str(j));
            fprintf(fid,',');                     
        end
        
    end
    if(u==1)
        fprintf(fid,'\n');
    end    
end
fclose(fid);
