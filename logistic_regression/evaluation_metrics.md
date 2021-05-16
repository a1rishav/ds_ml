# Evaluation Matrix

## Confusion Matrix and Accuracy
![confusion_matrix_and_accuracy](images/confusion_matrix_and_accuracy.png)

## Sensitivity and Specificity
![sensitivity_specificity](images/sensitivity_specificity.png)

## In Python
```buildoutcfg
# confusion matrix
from sklearn import metrics
confusion = metrics.confusion_matrix(y_train_pred_final.Churn, y_train_pred_final.predicted )
print(confusion)
print(metrics.accuracy_score(y_train_pred_final.Churn, y_train_pred_final.predicted))

TP = confusion[1,1] # true positive 
TN = confusion[0,0] # true negatives
FP = confusion[0,1] # false positives
FN = confusion[1,0] # false negatives
```
## ROC curve
![sensitivity_specificity](images/roc_curve.png)
- As True Positive Rate (sensitivity) increases False Positive (1 - Specificity) also increases or Specificity decreases 
- When area under the curve is more the model is better 
- ROC curve is a tradeoff between sensitvity and specificity
```buildoutcfg
def draw_roc( actual, probs ):
    fpr, tpr, thresholds = metrics.roc_curve( actual, probs,
                                              drop_intermediate = False )
    auc_score = metrics.roc_auc_score( actual, probs )
    plt.figure(figsize=(5, 5))
    plt.plot( fpr, tpr, label='ROC curve (area = %0.2f)' % auc_score )
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate or [1 - True Negative Rate]')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.show()

    return None

# Calling the function
draw_roc(y_train_pred_final.Churn, y_train_pred_final.Churn_Prob)
```
## Finding the Optimal Threshold
```buildoutcfg
# Now let's calculate accuracy sensitivity and specificity for various probability cutoffs.
cutoff_df = pd.DataFrame( columns = ['prob','accuracy','sensi','speci'])
from sklearn.metrics import confusion_matrix

# TP = confusion[1,1] # true positive 
# TN = confusion[0,0] # true negatives
# FP = confusion[0,1] # false positives
# FN = confusion[1,0] # false negatives

num = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
for i in num:
    cm1 = metrics.confusion_matrix(y_train_pred_final.Churn, y_train_pred_final[i] )
    total1=sum(sum(cm1))
    accuracy = (cm1[0,0]+cm1[1,1])/total1
    
    speci = cm1[0,0]/(cm1[0,0]+cm1[0,1])
    sensi = cm1[1,1]/(cm1[1,0]+cm1[1,1])
    cutoff_df.loc[i] =[ i ,accuracy,sensi,speci]
print(cutoff_df)
```
![sensitivity_specificity](images/sensitivity_specificity_tradeoff.png)
![sensitivity_specificity](images/tradeoff.png)
**The optimal cut-off point exists where the values of accuracy, sensitivity, and specificity are fairly decent and almost equal**

## Summary
![sensitivity_specificity](images/summary.png)

