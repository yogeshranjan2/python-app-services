information_security_risks_controls = [
{'RiskTitle': 'Failure to comply with policy requirements',
  'RiskDescription': 'Failure to adhere to the mandatory minimum information security requirements outlined in the policy.',
  'RiskCategory': 'Business Process Failure',
  'RiskControls': ['Control 1: Conduct regular training sessions on policy requirements for all employees and ensure acknowledgement of understanding.',
   'Control 2: Implement regular audits to verify policy compliance and take corrective actions for non-compliance.']},
 {'RiskTitle': 'Unauthorized access to sensitive information',
  'RiskDescription': 'Unauthorized individuals gaining access to sensitive information or systems.',
  'RiskCategory': 'Security Breach',
  'RiskControls': ['Control 1: Implement strong access control measures such as user authentication, role-based access permissions, and encryption of sensitive data.',
   'Control 2: Monitor and log all access attempts to sensitive information and systems for auditing and investigation purposes.']},
 {'RiskTitle': 'Lack of system backups and restoration plans',
  'RiskDescription': 'Failure to regularly backup critical information and implement reliable restoration plans in case of data loss.',
  'RiskCategory': 'Business Process Failure',
  'RiskControls': ['Control 1: Establish automated backup processes for critical data with regular testing of restoration procedures.',
   'Control 2: Implement separation of duties for backup and restoration functions to ensure accountability and accuracy.']},
 {'RiskTitle': 'Insufficient physical security measures',
  'RiskDescription': 'Inadequate security barriers and controls for physical facilities where information assets are stored.',
  'RiskCategory': 'Technology Failure',
  'RiskControls': ['Control 1: Deploy surveillance cameras and access control systems to monitor and restrict physical access to information processing and storage facilities.',
   'Control 2: Conduct periodic risk assessments to identify vulnerabilities in physical security and implement necessary enhancements.']},
 {'RiskTitle': 'Failure to perform vulnerability assessments',
  'RiskDescription': 'Neglecting to conduct regular vulnerability assessments on systems and networks leading to exploitable weaknesses.',
  'RiskCategory': 'Technology Failure',
  'RiskControls': ['Control 1: Implement automated vulnerability scanning tools to identify and prioritize security gaps for remediation.',
   'Control 2: Engage authorized individuals to perform periodic penetration tests to simulate real-world cyber attacks and evaluate defenses.']},
 {'RiskTitle': 'Poor incident response procedures',
  'RiskDescription': 'Lack of formal incident response plans and procedures to effectively address security incidents in a timely manner.',
  'RiskCategory': 'Security Breach',
  'RiskControls': ['Control 1: Develop and regularly update comprehensive incident response plans with clearly defined roles and responsibilities.',
   'Control 2: Conduct tabletop exercises and simulations to test the effectiveness of incident response procedures and improve response capabilities.']},
 {'RiskTitle': 'Inadequate user training on security best practices',
  'RiskDescription': 'Employees lacking awareness and understanding of security best practices, leading to higher vulnerability to cyber threats.',
  'RiskCategory': 'Business Process Failure',
  'RiskControls': ['Control 1: Provide regular security awareness training sessions covering common threats, safe practices, and reporting procedures.',
   'Control 2: Implement phishing simulations and quizzes to reinforce training and assess employee behavior in identifying potential threats.']},
 {'RiskTitle': 'Neglecting system maintenance and patching',
  'RiskDescription': 'Failure to regularly update and patch systems and software, leaving them exposed to known vulnerabilities.',
  'RiskCategory': 'Technology Failure',
  'RiskControls': ['Control 1: Establish automated patch management processes to deploy updates promptly and track patch status across all systems.',
   'Control 2: Perform regular vulnerability scans to identify unpatched systems and prioritize patching based on risk levels.']},
 {'RiskTitle': 'Shared account credentials usage',
  'RiskDescription': 'Multiple users sharing account credentials, making it difficult to attribute actions to specific individuals.',
  'RiskCategory': 'Security Breach',
  'RiskControls': ['Control 1: Enforce strict access control policies requiring individual user accounts for traceability of actions.',
   'Control 2: Implement multi-factor authentication to enhance account security and reduce the risk of unauthorized access.']},
 {'RiskTitle': 'Inadequate backup and disposal of sensitive data',
  'RiskDescription': 'Lack of proper procedures for backing up critical data and secure disposal of obsolete or sensitive information.',
  'RiskCategory': 'Business Process Failure',
  'RiskControls': ['Control 1: Implement regular data backup schedules with encryption and secure storage of backup copies.',
   'Control 2: Establish data retention and disposal policies to ensure sensitive information is securely erased or destroyed when no longer needed.']},
 {'RiskTitle': 'Insecure system configurations',
  'RiskDescription': 'Systems deployed with weak or insecure configurations, making them vulnerable to exploitation.',
  'RiskCategory': 'Technology Failure',
  'RiskControls': ['Control 1: Adhere to secure system configuration standards and conduct regular audits to verify compliance.',
   'Control 2: Implement automated configuration management tools to enforce and monitor system configurations for deviations or vulnerabilities.']},
 {'RiskTitle': 'Inadequate network segmentation',
  'RiskDescription': 'Lack of proper segmentation between network segments, increasing the risk of lateral movement by attackers.',
  'RiskCategory': 'Technology Failure',
  'RiskControls': ['Control 1: Implement network segmentation based on security zones to restrict unauthorized access between different network segments.',
   'Control 2: Conduct regular network architecture reviews to ensure segmentation aligns with security requirements and business needs.']},
 {'RiskTitle': 'Inadequate security logging and monitoring',
  'RiskDescription': 'Insufficient logging of security events and lack of real-time monitoring for detecting anomalous activities.',
  'RiskCategory': 'Security Breach',
  'RiskControls': ['Control 1: Deploy centralized logging systems to aggregate and analyze security event logs from various sources for proactive threat detection.',
   'Control 2: Implement real-time alerting mechanisms to notify security teams of suspicious activities or unauthorized access attempts.']},
 {'RiskTitle': 'Failure to document and maintain operating procedures',
  'RiskDescription': 'Lack of documented operating instructions and management procedures for critical systems and facilities.',
  'RiskCategory': 'Business Process Failure',
  'RiskControls': ['Control 1: Establish comprehensive operating procedures and incident management processes for all systems and facilities.',
   'Control 2: Regularly review and update operational documentation to reflect changes in systems and business processes.']},
 {'RiskTitle': 'Inadequate physical security controls',
  'RiskDescription': 'Lack of physical security measures such as surveillance cameras and access controls for information processing and storage facilities.',
  'RiskCategory': 'Technology Failure',
  'RiskControls': ['Control 1: Implement access control systems and surveillance cameras to monitor and restrict physical access to sensitive areas.',
   'Control 2: Conduct regular physical security assessments to identify vulnerabilities and implement necessary controls.']},
 {'RiskTitle': 'Data leakage due to lack of data handling controls',
  'RiskDescription': 'Unintentional or malicious data leakage due to improper handling of sensitive information.',
  'RiskCategory': 'Security Breach',
  'RiskControls': ['Control 1: Implement data classification and handling procedures to ensure appropriate security controls are applied to different data types.',
   'Control 2: Enforce data encryption for sensitive information in transit and at rest to prevent unauthorized access or disclosure.']},
 {'RiskTitle': 'Insufficient personnel security measures',
  'RiskDescription': 'Inadequate screening and monitoring of employees for access to sensitive information and assets.',
  'RiskCategory': 'Business Process Failure',
  'RiskControls': ['Control 1: Conduct background checks and suitability determinations for employees with access to sensitive information or assets.',
   'Control 2: Implement user access reviews and role-based training to ensure employees understand and follow security policies.']},
 {'RiskTitle': 'Failure to establish secure system development procedures',
  'RiskDescription': 'Lack of secure system development lifecycle practices leading to the deployment of vulnerable systems.',
  'RiskCategory': 'Technology Failure',
  'RiskControls': ['Control 1: Implement secure coding practices and perform code reviews to identify and address security vulnerabilities early in the development process.',
   'Control 2: Integrate security requirements into system development lifecycle stages and conduct security assessments before deployment.']},
 {'RiskTitle': 'Unauthorized network connections',
  'RiskDescription': 'Unauthorized connections between systems or networks without proper authorization and security controls.',
  'RiskCategory': 'Security Breach',
  'RiskControls': ['Control 1: Implement network access control measures to restrict unauthorized connections and monitor network traffic for anomalies.',
   'Control 2: Conduct regular reviews of network connections to verify authorization and compliance with security policies.']},
 {'RiskTitle': 'Failure to establish and test contingency plans',
  'RiskDescription': 'Lack of contingency plans and testing procedures for business continuity and disaster recovery scenarios.',
  'RiskCategory': 'Business Process Failure',
  'RiskControls': ['Control 1: Develop comprehensive business continuity and disaster recovery plans covering critical systems and operations.',
   'Control 2: Conduct regular tabletop exercises and simulations to validate contingency plans and identify areas for improvement.']},
 {'RiskTitle': 'Deficient operating security controls',
  'RiskDescription': 'Inadequate operational security controls such as access restrictions and data protection measures in place.',
  'RiskCategory': 'Technology Failure',
  'RiskControls': ['Control 1: Enforce access control policies and multi-factor authentication to restrict unauthorized access to systems and data.',
   'Control 2: Deploy endpoint security solutions and data loss prevention tools to secure critical information assets and prevent data breaches.']}
   ]