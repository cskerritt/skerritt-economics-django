# Settings Update Required

To enable the data-driven service list template, add the following context processor to your Django settings:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Add this line:
                'main.context_processors.services_config',
            ],
        },
    },
]
```

This will make the `services_config` variable available in all templates, allowing the service list to be dynamically generated from the centralized configuration.