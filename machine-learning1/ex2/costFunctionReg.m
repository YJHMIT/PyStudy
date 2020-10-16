function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

%J=-1/m*(y.*log(sigmoid(X*theta)+(1-y).*log(1-sigmoid(X*theta))))+lambda/m/2*sum(theta(2:end).^2);
%grad(1)=(sigmoid(X*theta-y))'*(X(:,1)/m;
%虽然j是从0开始的，但是在octave中都要从1开始下标
%for j=2:length(theta)
 % grad(j)=(sigmoid(X*theta)-y)'*(X(:,j)/m+lambda/m*theta(j);
%endfor  括号真的太烦了，多半个少半个的一直卡住

J = -1/m*sum(y.*log(sigmoid(X*theta))+(1-y).*log(1-sigmoid(X*theta)))+ lambda / 2 / m * sum(theta(2 : end).^2);
grad(1) =  X(:, 1)'*(sigmoid(X * theta) - y) / m;
for j=2:length(theta)
  grad(j)=(sigmoid(X*theta)-y)'*X(:,j)/m+lambda/m*theta(j);
endfor
% =============================================================

end
