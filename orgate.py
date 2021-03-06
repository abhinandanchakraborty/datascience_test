#(5.) Implement logical OR gate using neural network and scikit learn library
# - Reading:
# -- http://www.mind.ilstu.edu/curriculum/artificial_neural_net/neural_nets_for_logical_functions.php
# -- http://www.cs.bham.ac.uk/~jxb/NN/l3.pdf
# Note: You should create your own training and test datasets

from sklearn.neural_network import MLPClassifier
X = [[1., 1.], [0., 1.],[1.,0.],[0.,0.]]
y = [1, 1, 1, 0]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y) 
print(clf.predict([[2., 2.], [-2., -2.], [-5.,8.]]))
