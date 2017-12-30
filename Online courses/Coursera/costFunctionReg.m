function [cost, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples
[m,n] = size(X);

% You need to return the following variables correctly 
cost = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
sum = 0;
for i = 1:m
    h=0;
    for a = 1:n
        h = h+(theta(a) * X(i,a));
    end
    h=sigmoid(h);
    sum = sum + ((-y(i)*log(h)) - ((1-y(i)) * log(1-h)));
    
    for a=1:n
        grad(a) = grad(a) + ((h - y(i)) * X(i,a));
    end
end
cost = sum/m;
sum2=0;
for a = 1:n
    grad(a) = grad(a)/m;
    sum2 = sum2 + theta(a)^2;
end

for a = 2:n
    grad(a) = grad(a) + ((lambda/m) * theta(a));
end

cost = cost + ((lambda / (2*m)) * sum2);





% =============================================================

end
