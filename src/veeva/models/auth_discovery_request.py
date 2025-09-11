from pydantic import BaseModel, Field


class AuthDiscoveryRequest(BaseModel):
    """Request model for authentication discovery."""
    username: str = Field(..., description="The username for which to discover authentication methods.")
