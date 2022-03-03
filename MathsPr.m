X1=[2.5 0.5 2.2 1.9 3.1 2.3 2 1 1.5 1.1];

Y1=[ 2.4 0.7 2.9 2.2 3.0 2.7 1.6 1.1 1.6 0.9];
%REPRESENTATION VECTEURS
plot(X1,Y1,'+g');

X=[0.69 -1.31 0.39 0.09 1.29 0.49 0.19  -0.81 -0.31 -0.71];
disp("X:");
disp(X);

Y=[0.49 -1.21 0.99 0.29 1.09 0.79 -0.31 -0.81 -0.31 -1.01];
disp("Y:");
disp(Y);
%REPRESENTATION WITH MEAN SUBSTRACTED
hold on
plot(X,Y,'+');

%Matrive de covariance de X,Y
C=cov(X,Y);
disp("Matrice de covariance")
disp(C);
%Valeurs propres && vecteurs propres
disp("Valeurs propres");
vP=eig(C);
disp(vP);


disp("Vecteurs propres")   %don't have the same results ?! why? :(
[V,D] = eig(C);
disp(V);


FV=V(:,2:2);
disp("Valeurs propres");
disp(D);

disp("Feature vector")
disp(FV);

%STEP 5
%RowFeatureVector trasposé du feature vector
FV=transpose(FV);
disp("RowFeatureVector");
disp(FV);
%RowDataAdjust transpose of the original dataSet 
%==> Final data
FD=FV * transpose(X);
disp("Final Data");
disp(FD);




