# Logs Directory

This directory stores application logs.

## Log Files

- **rag_system.log** - Main RAG system operations and errors
- **debug.log** - Detailed debug information (when DEBUG=True)

## Log Levels

- **DEBUG**: Detailed information for debugging
- **INFO**: General informational messages
- **WARNING**: Warning messages for non-critical issues
- **ERROR**: Error messages for failures
- **CRITICAL**: Critical errors requiring immediate attention

## Configuration

Logs are configured in `src/utils/logger.py`

Enable DEBUG logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Viewing Logs

```bash
# View recent logs
tail -f logs/rag_system.log

# Search for errors
grep ERROR logs/rag_system.log

# Count warnings
grep -c WARNING logs/rag_system.log
```

## Cleanup

Archive old logs:
```bash
# Create archive
tar czf logs/archive_2024.tar.gz logs/*.log

# Remove old logs
find logs/ -name "*.log" -mtime +30 -delete
```

## Space Management

Keep logs under 100MB using logrotate or manual cleanup.
