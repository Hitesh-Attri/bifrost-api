from fastapi import APIRouter

from routers import groups, health, orgs, tenants, users

meta_router = APIRouter()

ORG_PREFIX = "/organizations/{org_id}"
ORG_TENANT_PREFIX = "/organizations/{org_id}/tenants/{tenant_id}"

# Global routes
meta_router.include_router(health.router)

# Org-level routes
meta_router.include_router(orgs.router)
meta_router.include_router(tenants.router, prefix=ORG_PREFIX)

# Org/tenant-scoped routes
meta_router.include_router(users.router, prefix=ORG_TENANT_PREFIX)
meta_router.include_router(groups.router, prefix=ORG_TENANT_PREFIX)
