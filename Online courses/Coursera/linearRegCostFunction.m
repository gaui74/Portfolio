function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples
[m,n] = size(X);

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%
sum = 0;
% Vector to save the values of h_theta(Xi)
h = zeros(size(y));
for i = 1:m
    for a = 1:n
        h(i) = h(i)+(X(i,a) * theta(a));
    end
end

for i = 1:m
    sum = sum + ((h(i)-y(i))^2);
    for a = 1:n
        grad(a) = grad(a) + ((h(i)-y(i)) * X(i,a));
    end
end
sum = sum/(2*m);
sum2 = 0;
for a=1:n
    grad(a) = grad(a)/m;
end

for a = 2:n
    sum2 = sum2 + (theta(a)^2);
    grad(a) = grad(a) + ((lambda/m)*theta(a));
end
sum2 = sum2*(lambda/(2*m));

J = sum + sum2;


% =========================================================================

end
