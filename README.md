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

POC初衷为，客户从自建Istio迁移至EKS，希望使用云原生服务网格，但因为AppMesh Virtual Gateway目前没有鉴权功能，希望能有替代方案。因此开展了此PoC验证可行性。

本次POC基于Api Gateway, NLB, App Mesh，自行实现了Virtual Gateway 的 JWT 鉴权。
POC 目标为验证使用API Gateway 为 App Mesh 添加 JWT 鉴权，并管理鉴权API黑白名单。
其中API gateway负责管理API和鉴权，NLB负责暴露EKS中App Mesh应用，App Mesh负责服务治理，EKS为应用运行环境。



源码介绍：
demoapi： 是为此POC准备的一个demo application，定义了/v1 和 /v2的多个API，用于验证黑白名单，/V1为黑名单，/V2为白名单
swagger.yaml: 是API Gateway配置文件，定义了鉴权的黑、白名单
appmesh: 应用部署的yaml配置文件

PoC 结论：
架构可行，可以使用API Gateway + NLB，或使用ALB为App Mesh添加JWT鉴权。
