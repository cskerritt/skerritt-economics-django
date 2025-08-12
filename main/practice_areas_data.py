"""
Comprehensive practice areas data for all services
Maps legal practice areas to specific services and applications
"""

PRACTICE_AREAS = {
    'personal-injury': {
        'name': 'Personal Injury',
        'slug': 'personal-injury',
        'description': 'Comprehensive economic and vocational analysis for personal injury litigation',
        'meta_description': 'Expert economic damage analysis, vocational assessment, and life care planning for personal injury cases. Forensic economics and business valuation services.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Damage Analysis for Personal Injury',
                'applications': [
                    'Lost earnings and earning capacity calculations',
                    'Fringe benefits valuation (health insurance, retirement, etc.)',
                    'Household services economic valuation',
                    'Present value and discount rate analysis',
                    'Inflation and wage growth projections',
                    'Tax impact considerations',
                    'Mitigation of damages analysis',
                    'Self-employment income loss calculations'
                ]
            },
            'vocational_expert': {
                'title': 'Vocational Assessment for Personal Injury',
                'applications': [
                    'Employability and placeability analysis',
                    'Transferable skills assessment',
                    'Labor market analysis and job availability',
                    'Functional capacity evaluation interpretation',
                    'Vocational rehabilitation planning',
                    'Return-to-work feasibility assessment',
                    'Job modification and accommodation analysis',
                    'Earning capacity evaluation pre and post-injury'
                ]
            },
            'life_care_planning': {
                'title': 'Life Care Planning for Personal Injury',
                'applications': [
                    'Future medical care needs projection',
                    'Rehabilitation services planning',
                    'Durable medical equipment requirements',
                    'Home modification specifications',
                    'Attendant care needs assessment',
                    'Medication and supply cost projections',
                    'Transportation and accessibility planning',
                    'Therapeutic and psychological services planning'
                ]
            },
            'business_valuation': {
                'title': 'Business Valuation in Personal Injury',
                'applications': [
                    'Self-employed plaintiff business valuation',
                    'Lost business value due to injury',
                    'Business interruption analysis',
                    'Key person valuation for business owners',
                    'Partnership interest valuation',
                    'Professional practice valuation',
                    'Goodwill and customer relationship impact',
                    'Business succession planning post-injury'
                ]
            }
        }
    },
    'motor-vehicle-accidents': {
        'name': 'Motor Vehicle Accidents',
        'slug': 'motor-vehicle-accidents',
        'description': 'Expert analysis for auto accident, trucking, and motorcycle collision cases',
        'meta_description': 'Economic damages, vocational assessment, and life care planning for motor vehicle accident cases. Expert witness services for MVA litigation.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Analysis for Motor Vehicle Accidents',
                'applications': [
                    'Lost wages from temporary and permanent disability',
                    'Future earning capacity reduction',
                    'Medical expense economic analysis',
                    'Vehicle and property damage valuation',
                    'Loss of household services valuation',
                    'Pain and suffering economic considerations',
                    'Wrongful death economic damages',
                    'Commercial driver lost earnings analysis'
                ]
            },
            'vocational_expert': {
                'title': 'Vocational Services for MVA Cases',
                'applications': [
                    'Post-accident work capacity assessment',
                    'Commercial driver license impact evaluation',
                    'Physical demands analysis for return to work',
                    'Cognitive function impact on employment',
                    'Traumatic brain injury vocational implications',
                    'Spinal injury employment assessment',
                    'Alternative employment options analysis',
                    'Vocational rehabilitation timeline and costs'
                ]
            },
            'life_care_planning': {
                'title': 'Life Care Planning for MVA Injuries',
                'applications': [
                    'Traumatic brain injury care planning',
                    'Spinal cord injury comprehensive planning',
                    'Multiple trauma care coordination',
                    'Orthopedic injury long-term care',
                    'Prosthetic and assistive device planning',
                    'Vehicle modification requirements',
                    'Chronic pain management planning',
                    'PTSD and psychological care planning'
                ]
            },
            'business_valuation': {
                'title': 'Business Impact of Motor Vehicle Accidents',
                'applications': [
                    'Commercial vehicle business impact',
                    'Fleet operation disruption analysis',
                    'Delivery service business losses',
                    'Transportation company valuation impact',
                    'Owner-operator income loss analysis',
                    'Franchise operation impact assessment',
                    'Partnership disruption valuation',
                    'Key employee loss business impact'
                ]
            }
        }
    },
    'medical-malpractice': {
        'name': 'Medical Malpractice',
        'slug': 'medical-malpractice',
        'description': 'Economic and vocational analysis for medical negligence and malpractice cases',
        'meta_description': 'Expert economic damage calculations and life care planning for medical malpractice cases. Forensic economics for healthcare litigation.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Damages in Medical Malpractice',
                'applications': [
                    'Birth injury lifetime economic impact',
                    'Surgical error economic consequences',
                    'Misdiagnosis financial damages',
                    'Medication error economic losses',
                    'Hospital negligence damage calculations',
                    'Loss of chance doctrine valuations',
                    'Additional medical expense projections',
                    'Wrongful death economic analysis'
                ]
            },
            'vocational_expert': {
                'title': 'Vocational Impact of Medical Malpractice',
                'applications': [
                    'Delayed diagnosis employment impact',
                    'Surgical complication work capacity',
                    'Birth injury lifetime vocational assessment',
                    'Medication error functional limitations',
                    'Healthcare professional disability evaluation',
                    'Pediatric injury future employability',
                    'Cognitive impairment vocational impact',
                    'Rehabilitation potential assessment'
                ]
            },
            'life_care_planning': {
                'title': 'Life Care Plans for Medical Malpractice',
                'applications': [
                    'Birth injury comprehensive care planning',
                    'Cerebral palsy lifetime care needs',
                    'Surgical complication remedial care',
                    'Anesthesia injury care requirements',
                    'Hospital-acquired infection treatment',
                    'Delayed diagnosis treatment planning',
                    'Medication error correction costs',
                    'Long-term facility care planning'
                ]
            },
            'business_valuation': {
                'title': 'Business Valuation in Medical Malpractice',
                'applications': [
                    'Medical practice valuation for provider cases',
                    'Healthcare business interruption',
                    'Professional reputation damage valuation',
                    'Medical professional lost earnings',
                    'Healthcare facility liability assessment',
                    'Medical partnership dissolution',
                    'Practice succession planning impact',
                    'Referral network valuation loss'
                ]
            }
        }
    },
    'workers-compensation': {
        'name': "Workers' Compensation",
        'slug': 'workers-compensation',
        'description': 'Comprehensive analysis for workplace injury and occupational disease claims',
        'meta_description': "Expert vocational and economic analysis for workers' compensation cases. Life care planning and return-to-work assessments.",
        'services': {
            'forensic_economics': {
                'title': "Economic Analysis for Workers' Compensation",
                'applications': [
                    'Permanent partial disability calculations',
                    'Total disability economic impact',
                    'Wage loss benefit analysis',
                    'Future medical cost projections',
                    'Vocational rehabilitation cost analysis',
                    'Third-party liability calculations',
                    'Pension and retirement impact',
                    'Union benefit loss calculations'
                ]
            },
            'vocational_expert': {
                'title': "Vocational Services for Workers' Comp",
                'applications': [
                    'Functional capacity evaluation',
                    'Job demands analysis',
                    'Transferable skills assessment',
                    'Labor market survey for suitable employment',
                    'Return-to-work planning and coordination',
                    'Job modification recommendations',
                    'Vocational rehabilitation planning',
                    'Maximum medical improvement assessment'
                ]
            },
            'life_care_planning': {
                'title': "Life Care Planning for Workplace Injuries",
                'applications': [
                    'Occupational disease treatment planning',
                    'Repetitive strain injury management',
                    'Industrial accident comprehensive care',
                    'Toxic exposure medical monitoring',
                    'Ergonomic equipment and modifications',
                    'Work hardening program planning',
                    'Chronic pain management programs',
                    'PTSD from workplace trauma'
                ]
            },
            'business_consulting': {
                'title': "Workplace Safety and Risk Consulting",
                'applications': [
                    'Safety program development and review',
                    'Workers compensation cost analysis',
                    'Return-to-work program design',
                    'Disability management consulting',
                    'OSHA compliance consulting',
                    'Ergonomic workplace assessment',
                    'Risk management strategies',
                    'Self-insurance feasibility analysis'
                ]
            }
        }
    },
    'employment-litigation': {
        'name': 'Employment Litigation',
        'slug': 'employment-litigation',
        'description': 'Economic analysis for wrongful termination, discrimination, and employment disputes',
        'meta_description': 'Expert economic damage calculations for employment litigation. Wrongful termination, discrimination, and wage loss analysis.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Damages in Employment Cases',
                'applications': [
                    'Wrongful termination lost earnings',
                    'Front pay and back pay calculations',
                    'Discrimination economic damages',
                    'Hostile work environment losses',
                    'Wage and hour violation calculations',
                    'Non-compete agreement damages',
                    'Executive compensation analysis',
                    'Stock option and equity valuation'
                ]
            },
            'vocational_expert': {
                'title': 'Vocational Analysis in Employment Disputes',
                'applications': [
                    'Mitigation of damages assessment',
                    'Job search effort evaluation',
                    'Comparable position analysis',
                    'Industry-specific employment options',
                    'Geographic labor market analysis',
                    'Retraining feasibility assessment',
                    'Career trajectory impact analysis',
                    'Professional reputation damage assessment'
                ]
            },
            'business_valuation': {
                'title': 'Business Valuation in Employment Cases',
                'applications': [
                    'Executive compensation benchmarking',
                    'Stock option valuation disputes',
                    'Deferred compensation valuation',
                    'Partnership interest disputes',
                    'Non-compete damage quantification',
                    'Trade secret misappropriation damages',
                    'Business opportunity loss valuation',
                    'Equity compensation analysis'
                ]
            },
            'business_consulting': {
                'title': 'HR and Employment Consulting',
                'applications': [
                    'Compensation structure analysis',
                    'HR policy development and review',
                    'Performance management systems',
                    'Succession planning strategies',
                    'Organizational restructuring impact',
                    'Diversity and inclusion programs',
                    'Employee retention strategies',
                    'Workplace culture assessment'
                ]
            }
        }
    },
    'product-liability': {
        'name': 'Product Liability',
        'slug': 'product-liability',
        'description': 'Economic and medical analysis for defective product and consumer injury cases',
        'meta_description': 'Expert economic damages and life care planning for product liability cases. Defective product injury analysis and valuation.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Analysis in Product Liability',
                'applications': [
                    'Consumer injury economic damages',
                    'Product recall cost analysis',
                    'Class action damage calculations',
                    'Manufacturing defect losses',
                    'Design defect economic impact',
                    'Warning defect damage assessment',
                    'Property damage valuations',
                    'Market share liability calculations'
                ]
            },
            'life_care_planning': {
                'title': 'Life Care Planning for Product Injuries',
                'applications': [
                    'Pharmaceutical injury care planning',
                    'Medical device failure treatment',
                    'Toxic exposure medical monitoring',
                    'Burn injury comprehensive care',
                    'Chemical exposure treatment planning',
                    'Food poisoning long-term effects',
                    'Defective implant revision surgeries',
                    'Pediatric product injury care'
                ]
            },
            'business_valuation': {
                'title': 'Business Impact of Product Liability',
                'applications': [
                    'Manufacturer liability assessment',
                    'Distributor chain impact analysis',
                    'Retailer liability valuation',
                    'Brand damage quantification',
                    'Recall cost business impact',
                    'Market share loss valuation',
                    'Supply chain disruption analysis',
                    'Insurance coverage dispute valuations'
                ]
            },
            'vocational_expert': {
                'title': 'Vocational Impact of Product Injuries',
                'applications': [
                    'Permanent disability from product defects',
                    'Chemical exposure work limitations',
                    'Burn injury employment impact',
                    'Prosthetic device failure vocational impact',
                    'Medication side effect work capacity',
                    'Toxic exposure career limitations',
                    'Repetitive strain from defective tools',
                    'Vision/hearing loss from products'
                ]
            }
        }
    },
    'premises-liability': {
        'name': 'Premises Liability',
        'slug': 'premises-liability',
        'description': 'Economic analysis for slip-and-fall, inadequate security, and property hazard cases',
        'meta_description': 'Expert economic damage calculations for premises liability cases. Slip and fall, security negligence, and property hazard analysis.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Damages in Premises Liability',
                'applications': [
                    'Slip and fall lost earnings',
                    'Inadequate security assault damages',
                    'Swimming pool accident losses',
                    'Construction site injury damages',
                    'Retail store accident economics',
                    'Apartment complex injury damages',
                    'Hotel and resort accident losses',
                    'Parking lot assault damages'
                ]
            },
            'vocational_expert': {
                'title': 'Vocational Assessment for Premises Injuries',
                'applications': [
                    'Fall injury work capacity assessment',
                    'Traumatic injury employment impact',
                    'Security assault PTSD vocational effects',
                    'Construction accident disability evaluation',
                    'Retail worker injury assessment',
                    'Hospitality worker injury evaluation',
                    'Maintenance worker disability analysis',
                    'Security guard injury assessment'
                ]
            },
            'life_care_planning': {
                'title': 'Life Care Plans for Premises Injuries',
                'applications': [
                    'Traumatic brain injury from falls',
                    'Spinal injury care planning',
                    'Multiple fracture treatment planning',
                    'Assault trauma comprehensive care',
                    'Dog bite injury treatment',
                    'Pool/drowning injury care needs',
                    'Burn injury from premises hazards',
                    'Lead paint exposure treatment'
                ]
            },
            'business_valuation': {
                'title': 'Property Business Impact Analysis',
                'applications': [
                    'Property management liability valuation',
                    'Commercial property damage assessment',
                    'Rental income loss calculations',
                    'Hotel/resort reputation damage',
                    'Retail location closure impact',
                    'Property value diminution',
                    'Insurance dispute valuations',
                    'Franchise location impact analysis'
                ]
            }
        }
    },
    'wrongful-death': {
        'name': 'Wrongful Death',
        'slug': 'wrongful-death',
        'description': 'Comprehensive economic analysis for wrongful death and survival action cases',
        'meta_description': 'Expert economic damage calculations for wrongful death cases. Lost earnings, household services, and family loss valuations.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Analysis in Wrongful Death',
                'applications': [
                    'Lifetime earnings loss calculations',
                    'Fringe benefits valuation to retirement',
                    'Household services economic value',
                    'Loss of consortium valuation',
                    'Personal consumption deductions',
                    'Inheritance and estate planning losses',
                    'Pension and Social Security losses',
                    'Child and spousal support calculations'
                ]
            },
            'vocational_expert': {
                'title': 'Vocational Analysis for Wrongful Death',
                'applications': [
                    'Career trajectory projection',
                    'Promotion probability analysis',
                    'Industry advancement patterns',
                    'Education completion probability',
                    'Self-employment potential assessment',
                    'Geographic mobility analysis',
                    'Worklife expectancy calculations',
                    'Retirement timing analysis'
                ]
            },
            'business_valuation': {
                'title': 'Business Valuation in Wrongful Death',
                'applications': [
                    'Business owner death valuation',
                    'Key person life insurance gaps',
                    'Partnership dissolution valuation',
                    'Succession planning failures',
                    'Professional practice wind-down',
                    'Closely-held business valuation',
                    'Intellectual property loss',
                    'Customer relationship valuations'
                ]
            },
            'life_care_planning': {
                'title': 'Survivor Care Planning',
                'applications': [
                    'Dependent child care planning',
                    'Elderly parent care arrangements',
                    'Special needs dependent planning',
                    'Grief counseling and support',
                    'Educational planning for dependents',
                    'Financial planning for survivors',
                    'Estate administration costs',
                    'Memorial and burial expenses'
                ]
            }
        }
    },
    'disability-insurance': {
        'name': 'Disability Insurance',
        'slug': 'disability-insurance',
        'description': 'Analysis for short-term, long-term, and Social Security disability claims',
        'meta_description': 'Expert vocational and economic analysis for disability insurance claims. SSDI, LTD, and private disability evaluation.',
        'services': {
            'vocational_expert': {
                'title': 'Vocational Assessment for Disability Claims',
                'applications': [
                    'Social Security Disability evaluation',
                    'Long-term disability assessment',
                    'Short-term disability evaluation',
                    'Veterans disability rating analysis',
                    'Private disability insurance claims',
                    'Residual functional capacity assessment',
                    'Any occupation vs. own occupation analysis',
                    'Surveillance video review and interpretation'
                ]
            },
            'forensic_economics': {
                'title': 'Economic Analysis for Disability Claims',
                'applications': [
                    'Disability benefit calculations',
                    'Offset analysis for multiple benefits',
                    'Cost of living adjustments',
                    'Taxation of disability benefits',
                    'Present value of future benefits',
                    'Rehabilitation cost-benefit analysis',
                    'Return-to-work financial impact',
                    'Pension disability calculations'
                ]
            },
            'life_care_planning': {
                'title': 'Care Planning for Disabled Individuals',
                'applications': [
                    'Chronic condition management planning',
                    'Progressive disease care projections',
                    'Mental health treatment planning',
                    'Substance abuse treatment programs',
                    'Assistive technology requirements',
                    'Home health care planning',
                    'Disability equipment and modifications',
                    'Long-term care facility planning'
                ]
            },
            'business_consulting': {
                'title': 'Disability Management Consulting',
                'applications': [
                    'Disability accommodation strategies',
                    'Return-to-work program development',
                    'Disability insurance plan design',
                    'ADA compliance consulting',
                    'Ergonomic assessment and planning',
                    'Disability prevention programs',
                    'Case management optimization',
                    'Benefits administration consulting'
                ]
            }
        }
    },
    'professional-liability': {
        'name': 'Professional Liability',
        'slug': 'professional-liability',
        'description': 'Economic analysis for professional malpractice and errors & omissions cases',
        'meta_description': 'Expert economic damage calculations for professional liability cases. Legal malpractice, accounting errors, and professional negligence.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Damages in Professional Liability',
                'applications': [
                    'Legal malpractice damage calculations',
                    'Accounting malpractice losses',
                    'Engineering errors economic impact',
                    'Architectural mistakes cost analysis',
                    'Financial advisor negligence damages',
                    'Real estate professional errors',
                    'Insurance broker liability damages',
                    'Technology professional negligence'
                ]
            },
            'business_valuation': {
                'title': 'Business Impact of Professional Errors',
                'applications': [
                    'Lost transaction valuations',
                    'Merger and acquisition failures',
                    'Tax planning error impacts',
                    'Investment opportunity losses',
                    'Contract negotiation failures',
                    'Intellectual property loss valuations',
                    'Regulatory compliance failures',
                    'Professional reputation damage'
                ]
            },
            'business_consulting': {
                'title': 'Professional Practice Consulting',
                'applications': [
                    'Risk management procedures',
                    'Quality control systems',
                    'Professional liability insurance review',
                    'Client engagement protocols',
                    'Documentation standards',
                    'Peer review processes',
                    'Continuing education planning',
                    'Succession planning for practices'
                ]
            },
            'vocational_expert': {
                'title': 'Professional Career Impact Analysis',
                'applications': [
                    'License suspension impact assessment',
                    'Professional reputation rehabilitation',
                    'Alternative career planning',
                    'Geographic practice limitations',
                    'Specialty restriction impacts',
                    'Supervision requirement analysis',
                    'Professional re-entry planning',
                    'Career transition assessment'
                ]
            }
        }
    },
    'construction-defects': {
        'name': 'Construction Defects',
        'slug': 'construction-defects',
        'description': 'Economic analysis for construction defect and building failure cases',
        'meta_description': 'Expert economic damage calculations for construction defect cases. Building failures, warranty claims, and repair cost analysis.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Analysis for Construction Defects',
                'applications': [
                    'Repair and replacement cost analysis',
                    'Diminution in property value',
                    'Loss of use and rental income',
                    'Relocation and temporary housing costs',
                    'Consequential damage calculations',
                    'Warranty claim valuations',
                    'Construction delay damages',
                    'Stigma damage quantification'
                ]
            },
            'business_valuation': {
                'title': 'Construction Business Impact Analysis',
                'applications': [
                    'Construction company liability assessment',
                    'Subcontractor default impacts',
                    'Developer reputation damage',
                    'Project financing impacts',
                    'Insurance coverage disputes',
                    'Performance bond claims',
                    'Mechanic lien valuations',
                    'Joint venture dispute resolution'
                ]
            },
            'business_consulting': {
                'title': 'Construction Business Consulting',
                'applications': [
                    'Project management systems review',
                    'Quality assurance program development',
                    'Subcontractor management strategies',
                    'Risk allocation in contracts',
                    'Insurance program optimization',
                    'Safety program development',
                    'Dispute resolution procedures',
                    'Project documentation standards'
                ]
            }
        }
    },
    'intellectual-property': {
        'name': 'Intellectual Property',
        'slug': 'intellectual-property',
        'description': 'Economic analysis for patent, trademark, copyright, and trade secret disputes',
        'meta_description': 'Expert economic damage calculations for intellectual property cases. Patent infringement, trademark disputes, and IP valuation.',
        'services': {
            'forensic_economics': {
                'title': 'Economic Damages in IP Cases',
                'applications': [
                    'Lost profits from infringement',
                    'Reasonable royalty calculations',
                    'Unjust enrichment analysis',
                    'Price erosion damages',
                    'Corrective advertising costs',
                    'Market share loss quantification',
                    'Convoyed sales analysis',
                    'Entire market value rule applications'
                ]
            },
            'business_valuation': {
                'title': 'Intellectual Property Valuation',
                'applications': [
                    'Patent portfolio valuation',
                    'Trademark valuation',
                    'Copyright valuation',
                    'Trade secret valuation',
                    'Technology transfer pricing',
                    'Licensing agreement valuation',
                    'IP holding company valuation',
                    'Royalty rate determination'
                ]
            },
            'business_consulting': {
                'title': 'IP Strategy Consulting',
                'applications': [
                    'IP portfolio management',
                    'Licensing strategy development',
                    'IP monetization strategies',
                    'Technology transfer planning',
                    'IP risk assessment',
                    'Competitive intelligence analysis',
                    'Innovation management systems',
                    'IP compliance programs'
                ]
            }
        }
    }
}

# Additional metadata for SEO
PRACTICE_AREA_CATEGORIES = {
    'personal_injury_related': [
        'personal-injury',
        'motor-vehicle-accidents',
        'medical-malpractice',
        'premises-liability',
        'product-liability',
        'wrongful-death'
    ],
    'employment_related': [
        'employment-litigation',
        'workers-compensation',
        'disability-insurance'
    ],
    'business_related': [
        'professional-liability',
        'construction-defects',
        'intellectual-property'
    ]
}

def get_practice_area(slug):
    """Get practice area data by slug"""
    return PRACTICE_AREAS.get(slug)

def get_all_practice_areas():
    """Get all practice areas"""
    return PRACTICE_AREAS

def get_practice_areas_for_service(service_slug):
    """Get all practice areas that use a specific service"""
    areas = []
    for area_slug, area_data in PRACTICE_AREAS.items():
        if service_slug in area_data.get('services', {}):
            areas.append({
                'slug': area_slug,
                'name': area_data['name'],
                'description': area_data['services'][service_slug].get('title', '')
            })
    return areas