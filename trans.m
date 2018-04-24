function trans(p)
fid = fopen('data3.txt','wt');
fprintf(fid,'@relation');
for j=1:1682
    
    fprintf(fid,'@attribute ');
    fprintf(fid,int2str(j-1));
    fprintf(fid,'\n');
end    

for i=1:944
    for j=1:1682
        if p(i,j)>3
            if j==1682
                fprintf(fid,'y');
            else
                fprintf(fid,'y,');
            end    
        else 
            if j==1682
                fprintf(fid,'n');
            else
                fprintf(fid,'n,');
            end
        end
        
    end
    fprintf(fid,'\n');
end
fclose(fid);
