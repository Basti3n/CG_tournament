import logging
import logging.config


def setup_logging_configuration(s_log_level: str, s_process_name: str) -> None:
    s_path = './logs'
    s_filename_path = f'{s_path}/{s_process_name}.log'

    dc_config_logger = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s'
            }
        },
        'handlers': {
            'log_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': s_log_level,
                'formatter': 'simple',
                'filename': s_filename_path,
                'maxBytes': 50000000,
                'backupCount': 1,
                'encoding': 'utf8'
            },
            'log_console': {
                'class': 'logging.StreamHandler',
                'level': s_log_level,
                'formatter': 'simple'
            }
        },
        'root': {
            'level': s_log_level,
            'handlers': ['log_file', 'log_console']
        }
    }

    logging.config.dictConfig(dc_config_logger)