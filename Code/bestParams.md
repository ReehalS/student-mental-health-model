# A compiled list of all the best parameters for the 
## KNN

Major:  business
Best Parameters: {'algorithm': 'auto', 'leaf_size': 20, 'metric': 'manhattan', 'n_jobs': -1, 'n_neighbors': 18, 'weights': 'uniform'}
Best Cross-Validation Accuracy: 0.8041406575114441
Test Set Accuracy: 0.7877094972067039

Major:  engineering
Best Parameters: {'algorithm': 'auto', 'leaf_size': 20, 'metric': 'manhattan', 'n_jobs': -1, 'n_neighbors': 16, 'weights': 'uniform'}
Best Cross-Validation Accuracy: 0.8087943739946882
Test Set Accuracy: 0.7790262172284644

Major:  law
Best Parameters: {'algorithm': 'auto', 'leaf_size': 20, 'metric': 'minkowski', 'n_jobs': -1, 'n_neighbors': 14, 'weights': 'uniform'}
Best Cross-Validation Accuracy: 0.7990377290854506
Test Set Accuracy: 0.8034682080924855

Major:  medical
Best Parameters: {'algorithm': 'auto', 'leaf_size': 20, 'metric': 'minkowski', 'n_jobs': -1, 'n_neighbors': 17, 'weights': 'uniform'}
Best Cross-Validation Accuracy: 0.8142493638676845
Test Set Accuracy: 0.7786259541984732

Major:  others
Best Parameters: {'algorithm': 'auto', 'leaf_size': 20, 'metric': 'manhattan', 'n_jobs': -1, 'n_neighbors': 12, 'weights': 'uniform'}
Best Cross-Validation Accuracy: 0.7869330004161466
Test Set Accuracy: 0.7877094972067039

## SVC
Major: business
Best Parameters: {'C': 0.1, 'gamma': 'scale', 'kernel': 'linear'}
Grid Search Score: 0.80246
Mean Cross-Validation Score: 0.80244

Major: engineering
Best Parameters: {'C': 0.1, 'gamma': 'scale', 'kernel': 'linear'}
Grid Search Score: 0.80422
Mean Cross-Validation Score: 0.80419

Major: law
Best Parameters: {'C': 0.1, 'gamma': 'scale', 'kernel': 'linear'}
Grid Search Score: 0.79982
Mean Cross-Validation Score: 0.79978

Major: medical
Best Parameters: {'C': 0.1, 'gamma': 'scale', 'kernel': 'linear'}
Grid Search Score: 0.80549
Mean Cross-Validation Score: 0.80549

Major: others
Best Parameters: {'C': 0.1, 'gamma': 'scale', 'kernel': 'linear'}
Grid Search Score: 0.79159
Mean Cross-Validation Score: 0.79156

## Neural Networks:

For Threshold of 3
For business , Best: 0.802000 using {'batch_size': 32, 'model__activation': 'relu', 'model__learning_rate': 0.001, 'model__momentum': 0.5, 'model__num_layers': 4, 'model__num_neurons': 10, 'model__reg_method': 'l1', 'model__reg_rate': 0.001}
For engineering , Best: 0.809709 using {'batch_size': 32, 'model__activation': 'relu', 'model__learning_rate': 0.001, 'model__momentum': 0.5, 'model__num_layers': 3, 'model__num_neurons': 12, 'model__reg_method': 'l1', 'model__reg_rate': 0.01}
For law , Best: 0.801261 using {'batch_size': 32, 'model__activation': 'relu', 'model__learning_rate': 0.001, 'model__momentum': 0.5, 'model__num_layers': 3, 'model__num_neurons': 10, 'model__reg_method': 'l2', 'model__reg_rate': 0.001}
For medical , Best: 0.808447 using {'batch_size': 32, 'model__activation': 'relu', 'model__learning_rate': 0.001, 'model__momentum': 0.5, 'model__num_layers': 2, 'model__num_neurons': 8, 'model__reg_method': 'l1', 'model__reg_rate': 0.001}
For others , Best: 0.789515 using {'batch_size': 32, 'model__activation': 'relu', 'model__learning_rate': 0.001, 'model__momentum': 0.5, 'model__num_layers': 3, 'model__num_neurons': 8, 'model__reg_method': 'l1', 'model__reg_rate': 0.01}

## Random Forest:

Major: business
Best Parameters: {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200}
Grid Search Score: 0.72444
Mean Cross-Validation Score: 0.73204

Major: engineering
Best Parameters: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100}
Grid Search Score: 0.71214
Mean Cross-Validation Score: 0.71136

Major: law
Best Parameters: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 100}
Grid Search Score: 0.69991
Mean Cross-Validation Score: 0.67723

Major: medical
Best Parameters: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 200}
Grid Search Score: 0.70630
Mean Cross-Validation Score: 0.69519

Major: others
Best Parameters: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 200}
Grid Search Score: 0.73343
Mean Cross-Validation Score: 0.71345

## Logistic Regression:

Major: business
Best Parameters: {'C': 0.01, 'max_iter': 100, 'penalty': 'l1', 'solver': 'liblinear'}
Grid Search Score: 0.8024561403508772
Mean Cross-Validation Score: 0.80244

Major: engineering
Best Parameters: {'C': 0.01, 'max_iter': 100, 'penalty': 'l1', 'solver': 'liblinear'}
Grid Search Score: 0.8042242862057103
Mean Cross-Validation Score: 0.80419

Major: law
Best Parameters: {'C': 0.01, 'max_iter': 100, 'penalty': 'l1', 'solver': 'liblinear'}
Grid Search Score: 0.7998190045248869
Mean Cross-Validation Score: 0.79978

Major: medical
Best Parameters: {'C': 0.01, 'max_iter': 100, 'penalty': 'l1', 'solver': 'liblinear'}
Grid Search Score: 0.8054904051172708
Mean Cross-Validation Score: 0.80549

Major: others
Best Parameters: {'C': 0.01, 'max_iter': 100, 'penalty': 'l1', 'solver': 'liblinear'}
Grid Search Score: 0.7915942028985509
Mean Cross-Validation Score: 0.79156

## Naive Bayes:

Major: business
Best Parameters: {'var_smoothing': 1e-09}
Grid Search Score: 0.56210
Mean Cross-Validation Score: 0.57406

Major: engineering
Best Parameters: {'var_smoothing': 1e-09}
Grid Search Score: 0.57874
Mean Cross-Validation Score: 0.57797

Major: law
Best Parameters: {'var_smoothing': 1e-09}
Grid Search Score: 0.51700
Mean Cross-Validation Score: 0.51868

Major: medical
Best Parameters: {'var_smoothing': 1e-09}
Grid Search Score: 0.50778
Mean Cross-Validation Score: 0.51704

Major: others
Best Parameters: {'var_smoothing': 1e-09}
Grid Search Score: 0.52103
Mean Cross-Validation Score: 0.49665

## SGD

Major:  business
Best parameters found:  {'alpha': 0.0001, 'eta0': 1.0, 'learning_rate': 'constant', 'loss': 'squared_hinge', 'max_iter': 3000, 'penalty': 'l2'}
Best cross-validation accuracy:  0.8025019069412662
Test set accuracy:  0.8041958041958042

Major:  engineering
Best parameters found:  {'alpha': 0.01, 'eta0': 1.0, 'learning_rate': 'constant', 'loss': 'squared_hinge', 'max_iter': 3000, 'penalty': 'l2'}
Best cross-validation accuracy:  0.8124251805985552
Test set accuracy:  0.7757009345794392

Major:  law
Best parameters found:  {'alpha': 0.001, 'eta0': 1.0, 'learning_rate': 'constant', 'loss': 'squared_hinge', 'max_iter': 3000, 'penalty': 'l1'}
Best cross-validation accuracy:  0.7998190045248869
Test set accuracy:  0.8050541516245487

Major:  medical
Best parameters found:  {'alpha': 0.0001, 'eta0': 0.01, 'learning_rate': 'adaptive', 'loss': 'perceptron', 'max_iter': 3000, 'penalty': 'l2'}
Best cross-validation accuracy:  0.8126510305614782
Test set accuracy:  0.7476190476190476

Major:  others
Best parameters found:  {'alpha': 0.001, 'eta0': 0.01, 'learning_rate': 'constant', 'loss': 'perceptron', 'max_iter': 3000, 'penalty': 'l2'}
Best cross-validation accuracy:  0.7986117467581998
Test set accuracy:  0.25874125874125875
