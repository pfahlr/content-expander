# This project will provide the basic requirements for a SaaS product. 

- REST API Based Operation provides loose coupling from the front-end. It should be possible to create any sort of front-end you desire. React? Android/iOS app? etc [component](/backend/fastapi) [design notes](./backend/fastapi/)
  - Python FastAPI
  - User Management through FastAPI-Users Module
      - Bearer Transport (using session storage) JWT Strategy, using Elliptic Curve Asymmetric Key Encryption "ES256" - (Default Configuration, can be easily changed to your preference)
  - ORM and Validation with SQLModel/SQLAlchemy/Pydantic
  - Login from Google
  - Messaging Class for sending email and sms from a variety of services.
  - [TODO] Subscription/Credit System Handling
    - [TODO] Stripe Payment Gateway
    - [TODO] Cryptocurrency Payment Gateway
    
- PostgreSQL 17 database container [component](/database/) [design-notes](./database/)
- React + Vite Base Frontend [component](./frontend/content-expander-frontend/) [design notes](./frontend/react-web/)
- [TODO] React Native Frontend [component](./frontend/react-native/) [design notes](./frontend/react-native/)
- [TODO] AstroJS Marketing Site [component](./marketing/) [design notes](./astrojs/)
    - Landing Page System
    - Blog System


  

  
