# Kubernetes exercises

Example Voting App:
https://github.com/PXL-Systems-Expert/example-voting-app.git

## ConfigMaps

1. Delete the vote Deployment to manage the environment variables using ConfigMaps.
1. Create a ConfigMaps resource to externalize certain configurations of the vote Pods:
1. Name the ConfigMaps "vote".
1. The ConfigMaps should manage the following data:
   - option_a: "CATS"
   - option_b: "DOGS"
1. Update the Deployment of the vote Pods to link the ConfigMaps as environment variables:
   - The name of the environment variable for option_a should be OPTION_A.
   - The name of the environment variable for option_b should be OPTION_B.
