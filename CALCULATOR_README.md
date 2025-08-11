# Economic Damages Calculator - Setup Guide

## Overview
The Economic Damages Calculator has been successfully integrated into your Django application. It provides a comprehensive web-based tool for calculating economic damages using the Tinari (AEF/AIF) method.

## Features Implemented

### 1. User Authentication
- **Registration**: New users can create accounts with email verification
- **Login/Logout**: Secure authentication system
- **Password Protection**: All calculator features require authentication

### 2. Database Models (PostgreSQL Ready)
- **EconomicScenario**: Main model storing all calculation parameters
- **ActualEarnings**: Historical earnings data import
- **CalculationHistory**: Audit trail of all calculations
- **ManualOffsetEntry**: Manual adjustment capabilities

### 3. Calculator Features
- **Tinari Method Implementation**: Full AEF/AIF calculations
- **Pediatric Cases**: Support for workforce entry calculations
- **Growth Timing Options**: End-of-year, mid-year, or continuous
- **Jurisdiction Presets**: FL, NY, and Federal defaults
- **Present Value Calculations**: With customizable discount rates
- **CSV Import/Export**: For actual earnings data
- **Scenario Management**: Save, load, and export scenarios as JSON

### 4. User Interface
- **Dashboard**: Overview of all user scenarios
- **Calculator Form**: Comprehensive input interface
- **Real-time Calculations**: AJAX-based calculation without page refresh
- **Results Tables**: Pre-injury and post-injury wage loss tables
- **Export Options**: CSV exports for all tables and factors

## Setup Instructions

### 1. Install Dependencies
```bash
pip install psycopg2-binary python-dateutil
```

### 2. Database Configuration

#### For PostgreSQL (Production):
1. Create a PostgreSQL database:
```sql
CREATE DATABASE economic_damages;
CREATE USER your_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE economic_damages TO your_user;
```

2. Set environment variable:
```bash
export USE_POSTGRES=True
```

3. Update `.env` file with your database credentials:
```
DB_NAME=economic_damages
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

#### For SQLite (Development):
No additional setup needed - SQLite is used by default when `USE_POSTGRES` is not set.

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Access the Application

Start the development server:
```bash
python manage.py runserver
```

Navigate to:
- Calculator: `http://localhost:8000/calculator/`
- Admin Panel: `http://localhost:8000/admin/`

## Usage Guide

### Creating a New Scenario
1. Login to the calculator
2. Click "New Scenario" from the dashboard
3. Fill in the required fields:
   - Front matter (plaintiff info, dates)
   - Wages and growth rates
   - Durations (life expectancy, work-life expectancy)
   - Factors (WLF, UF, TR, FB, PC)
4. Save the scenario
5. Click "Calculate" to run the calculations

### Exporting Results
- **CSV Export**: Export pre-injury, post-injury, or factors tables
- **JSON Export**: Export entire scenario for backup or sharing
- **Import**: Load previously exported scenarios

### Manual Adjustments
- Post-injury offset amounts can be manually adjusted in the results table
- Lock specific years to prevent recalculation

## Production Deployment

### Environment Variables
Copy `.env.example` to `.env` and update:
```bash
cp .env.example .env
# Edit .env with your production values
```

### Static Files
```bash
python manage.py collectstatic
```

### Security Considerations
1. Always use PostgreSQL in production
2. Set `DEBUG=False` in production
3. Use strong `SECRET_KEY`
4. Configure proper ALLOWED_HOSTS
5. Use HTTPS (SSL/TLS) in production
6. Regular database backups

## API Endpoints

The calculator provides several API endpoints:

- `POST /calculator/api/<scenario_id>/calculate/` - Run calculations
- `POST /calculator/api/<scenario_id>/manual-offset/` - Save manual offsets
- `POST /calculator/api/<scenario_id>/import-actuals/` - Import CSV actuals
- `GET /calculator/<scenario_id>/export/<table_type>/` - Export CSV
- `GET /calculator/<scenario_id>/export-scenario/` - Export JSON
- `POST /calculator/import-scenario/` - Import JSON scenario

## Testing

Test credentials (development only):
- Username: `admin`
- Password: `admin123`

## Troubleshooting

### Database Connection Issues
- Verify PostgreSQL is running: `sudo systemctl status postgresql`
- Check credentials in `.env` file
- Ensure database exists and user has permissions

### Missing Dependencies
```bash
pip install -r requirements.txt
```

### Migration Issues
```bash
python manage.py makemigrations calculator
python manage.py migrate
```

## Support

For issues or questions about the calculator implementation, please review the code in:
- Models: `/calculator/models.py`
- Views: `/calculator/views.py`
- Calculations: `/calculator/calculations.py`
- Templates: `/calculator/templates/calculator/`

## License

This calculator is integrated into your existing Django application and follows your project's licensing terms.