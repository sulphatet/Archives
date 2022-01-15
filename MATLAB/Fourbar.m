l1 = 5;
l2 = 3;
l3 = 7;
l4 = 6;

th2 = 0.1:0.1:25;
thts = zeros(2,length(th2)+1);


for i = 1:length(th2)
    funhandle = @(x) loop(x,th2(i),l1,l2,l3,l4);
    thts(:,i+1) = fsolve(funhandle,thts(:,i)); 
end

th3 = thts(1,2:end);
th4 = thts(2,2:end);

%% Plotting

xmin = -10;
ymin = xmin;
xmax = 15;
ymax = xmax;

figure;
axis([xmin,xmax,ymin,ymax]);

o1 = [0;0];
o4 = [l1;0];
R2 = [l2*cos(th2);l2*sin(th2)];
R3 = [R2(1,:)+l3*cos(th3);R2(2,:)+l3*sin(th3)];

for i = 1:length(th2)
    clf;
    plot([o1(1),o4(1)], [o1(2),o4(2)], 'k--','LineWidth',3); %groundlink
    plot([o1(1),R2(1,1)], [o1(2),R2(2,i)],'-b','LineWidth',3); %link1
    plot([R2(1,i),R3(1,i)], [R2(2,i),R3(2,i)],'r','LineWidth',3);%link2
    plot([R3(1,i),o4(1)], [R3(2,i),o4(2)],'r','LineWidth',3);%link4
    plot([o1(1),R2(1,i),R3(1,i),o4(1)],[o1(2),R2(2,i),R3(2,i),o4(2)],'ko');
    hold off;

    axis([xmin,xmax,ymin,ymax]);
    pause(0.001);
end

%% LOOP CLOSURE EQN
function vals = loop(unks,th2,l1,l2,l3,l4)

loopx = l2*cos(th2) + l3*cos(unks(1)) -l1 -l4*cos(unks(2));
loopy = l2*sin(th2) + l3*sin(unks(1)) -l4*sin(unks(2));

vals = [loopx;loopy];

end

%% 
%     iffi ==1
%         initvals = [0;0];
%     
%         intvals = thts(:,i+1)
%     and
%     funhandle = @(unk) loop(unk,th2(1),l1,l2,l3,l4);
% thts(:,i+1) = fsolve(funhandle,thts(:,i)); 
%  
