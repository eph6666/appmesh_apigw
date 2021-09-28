# appmesh_apigw

JSON Web Token（JWT）是目前最流行的跨域认证解决方案。用户在使用 App Mesh 或直接使用 EKS 部署应用时会面临需要身份验证的情况，使用JWT能够有效解决这个问题。

AWS App Mesh 是一种服务网格，可提供应用程序级网络，让您的服务可以轻松跨多种类型的计算基础设施相互通信。App Mesh 可以与 AWS上运行的 AWS Fargate、Amazon EC2、Amazon ECS、Amazon EKS 和 Kubernetes 以及 AWS Outposts 配合使用，以更好地大规模运行您的应用程序。

App  Mesh 由以下组件构成：

- Service Mesh
- Virtual gateways and Gateway routes
- Virtual services
- Virtual nodes
- Virtual routers and routes
- Proxy (Envoy)

其中Virtual gateways是虚拟网关允许网格外部的资源与网格内部的资源进行通信。（关于其他组件的详细介绍可以参考[文档](https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html)）

目前Virtual gateways本身不支持身份验证等功能。随着Istio等方案迁移至App Mesh的用户越来越多，服务网格的身份验证成为一个问题。

本次POC基于Api Gateway, NLB, App Mesh，自行实现了Virtual Gateway 的 JWT 鉴权。

源码介绍：
demoapi： 是一个demo application，定义了/v1 和 /v2的多个API
swagger.yaml: 是API Gateway配置文件，定义了鉴权的黑、白名单
appmesh: 应用部署的yaml配置文件
