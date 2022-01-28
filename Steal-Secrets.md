## Steal Secrets

| **Note** Replace `serverip` wherever neccessary

* Step 1: Change to directory

    ```
    cd /root/kube-steal-secrets
    ```

    ```
    chmod +x setup-kube.sh
    ```

    ```
    sh setup-kube.sh
    ```

* Step 2: Create resources

    ```
    kubectl apply -f xxe-manifest.yml
    ```

* Step 3: Access your service with this url

    ```
    http://<serverip>:32345
    ```

    Replace `<serverip>` with your virtual machine ip

    * To get server ip type the following command in terminal

        ```
        serverip
        ```    

* Step 4: Now upload the `users.xml` file, you should see user listed out on the screen

* Step 5: Now upload the `malicious.xml` file, you will get the `ServiceAccount` token

* Step 6: Now use the `ServiceAccount` token to get other cluster information

* Step 7: Destroy resources

    ```
    kubectl delete -f xxe-manifest.yml
    ```