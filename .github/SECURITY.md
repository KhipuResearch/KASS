# Security Policy

## Supported Versions

KASS notebooks are continuously updated. We support:

| Version | Supported          |
| ------- | ------------------ |
| Latest main branch | ✅ |
| Older commits | ❌ (use latest) |

## Reporting a Vulnerability

**Do NOT report security vulnerabilities through public issues, discussions, or pull requests.**

### For Security Issues:

**Email:** security@krlabs.dev

**Include:**
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

**Response timeline:**
- **Acknowledgment:** Within 48 hours
- **Assessment:** Within 7 days
- **Fix timeline:** Depends on severity (critical: days, high: weeks, low: next release)

### What Qualifies as a Security Issue?

**Yes:**
- Exposure of sensitive data (API keys, credentials, PII)
- Code execution vulnerabilities
- Privilege escalation
- Data injection attacks
- Malicious code in dependencies

**No (use regular issues instead):**
- Bugs that don't affect security
- Feature requests
- Documentation errors
- Performance issues

## Security Best Practices

When using KASS notebooks:

1. **Never commit credentials:**
   - Use environment variables for API keys
   - Add `.env` to `.gitignore`
   - Use secrets management for production

2. **Validate data sources:**
   - Verify data connector URLs
   - Check SSL certificates
   - Use official API endpoints only

3. **Review dependencies:**
   - Keep packages updated
   - Check for known vulnerabilities with `pip-audit`
   - Pin versions in production

4. **Data handling:**
   - Never include real PII in example notebooks
   - Sanitize data before sharing
   - Follow data use agreements

5. **KRL Platform users:**
   - Use SSO when available
   - Enable 2FA
   - Follow organizational security policies

## Disclosure Policy

We follow **responsible disclosure**:

1. Reporter submits vulnerability privately
2. We confirm and develop fix
3. We deploy fix to repository
4. We publicly disclose after fix is deployed (typically 90 days)
5. We credit reporter (unless they prefer anonymity)

## Security Updates

Critical security updates are announced:
- GitHub Security Advisories
- Repository README banner
- Project Discussions

Subscribe to repository notifications to stay informed.

## Contact

- **Security issues:** security@krlabs.dev
- **General questions:** Open a [Discussion](../../discussions)
- **Platform security:** https://krlabs.dev/security

---

**Thank you for helping keep KASS and its users safe.**
