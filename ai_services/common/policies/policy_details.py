information_security_policy_text = """
Policies, Standards, and Procedures

Information security policies, standards, and procedures should define the institution control
environment through a governance structure and provide descriptions of required, expected, and
prohibited activities. Policies, standards, and procedures guide decisions and activities of users,
developers, administrators, and managers and inform those individuals of their information
security responsibilities. Policies, standards, and procedures should also specify the mechanisms
through which responsibilities can be met. In addition, they should provide guidance on
acquiring, designing, implementing, configuring, operating, maintaining, and auditing
information systems. Policies, standards, and procedures that address the information security
program should describe the roles of the information security department, lines of business, and
IT organization in administering the information security program. Information security policies,
standards, and procedures form the means by which the objectives of the information security
program are achieved.

Technology Design
While technology can introduce risk, it can also serve as a mitigation tool. Management should
understand the benefits and limitations of the technology that the institution uses and whether
other types of controls are necessary to compensate for those limitations.
Information security issues arise when (a) the design of the technology and the policies
governing its use do not effectively defend against identified and unidentified threats, (b) threats
change in ways not envisioned by the designers, and (c) the controls are not operating as
intended. Management should continually assess the capability of the institution processes,
people, and technologies to sustain the appropriate level of information security based on the
institutions risk profile, size, complexity, and risk appetite

Control Types
Management may mitigate information security risks by implementing controls. Controls may be
categorized according to timing and nature. It is important to have a layered control system, which deploys 
different controls at different points of a business process and throughout an IT system so that the strength of 
one control can compensate for weaknesses in or possible failure of another control. Therefore, layered controls
function in an integrated fashion to more effectively mitigate risk.
Economic and technical considerations generally affect prevention and detection or response
choices in system design. Compensating controls are controls that adjust for weaknesses within
the system or process. An example of compensating controls would be a review of activity logs
for applications that do not allow proper segregation of duties.

Control Implementation
Management should implement controls that align security with the nature of the institution
operations and strategic direction. Based on the institution risk assessment, the controls should
include, but may not be limited to, patch management, asset and configuration management,
vulnerability scanning and penetration testing, end-point security, resilience controls, logging
and monitoring, and secure software development (including third-party software development).
In implementing controls, management should ensure it has the necessary resources, personnel
training, and testing to maximize the effectiveness of the controls.
The level at which controls are implemented should depend on the institution size, complexity,
and risk profile, but all institutions should implement appropriate controls. In light of increasing
cybersecurity risks, management should implement risk-based controls for managing
cybersecurity threats and vulnerabilities, such as interconnectivity risk. Management should
review and update the security controls as necessary depending on changes to the internal and
external operating environment, technologies, business processes, and other factors.

User Security Controls

Users should be granted access to systems, applications, and databases based on their job
responsibilities. Access rights should be granted in accordance with the institution physical and
logical access control policies. Authorized users with elevated or administrator privileges can
pose a potential threat to systems and data. Employees, contractors, or third-party service
providers can exploit their legitimate computer access for unauthorized purposes. Additionally,
the degree of internal access granted to some users increases the risk of damage or loss of
information and systems

Segregation of Duties

Segregation of duties, or job designs that require more than one person to complete critical or
sensitive tasks, can help mitigate risk. Employees and third parties with access to sensitive
resources could cause substantial damage and potential loss. System administrators, for instance,
have the most powerful role in the user access process and have unlimited access to an
institution information assets and technology. Given this extensive access, management should
evaluate the process for determining which individuals should be granted system administrator
privileges. Such access should be appropriately monitored for unauthorized or inappropriate
activity

Network Controls
Networks should be protected by a secure boundary, identifying “trusted” and “untrusted” zones.
Internal zones, typically trusted, should segregate various components into distinct areas, each
with the level of controls appropriate to the content and function of the assets within the zone.
The institutions trusted network should be protected through appropriate configuration and
patch management, privileged access controls, segregation of duties, implementation of effective
security policies, and use of perimeter devices and systems to prevent and detect unauthorized
access. Tools used to enforce and detect perimeter protection include routers, firewalls, intrusion
detection systems (IDS) and intrusion prevention systems, proxies, gateways, jump boxes,25
demilitarized zones, virtual private networks (VPN), virtual LANs (VLAN), log monitoring and
network traffic inspecting systems, data loss prevention (DLP) systems, and access control lists.
"""

application_development_policy_text = """

Software Development Life Cycle:
The systems development life cycle is a project management technique that divides
complex projects into smaller, more easily managed segments or phases. Segmenting
projects allows managers to verify the successful completion of project phases before
allocating resources to subsequent phases.
Software development projects typically include initiation, planning, design, development,
testing, implementation, and maintenance phases. However, the phases may be divided
differently depending on the organization involved. For example, initial project activities
might be designated as request, requirements-definition, and planning phases, or
initiation, concept-development, and planning phases. End users of the system under
development should be involved in reviewing the output of each phase to ensure the
system is being built to deliver the needed functionality.

Initiation Phase
Careful oversight is required to ensure projects support strategic business objectives and
resources are effectively implemented into an organization's enterprise architecture. The
initiation phase begins when an opportunity to add, improve, or correct a system is
identified and formally requested through the presentation of a business case. The
business case should, at a minimum, describe a proposal's purpose, identify expected
benefits, and explain how the proposed system supports one of the organization's
business strategies. The business case should also identify alternative solutions and
detail as many informational, functional, and network requirements as possible.
The presentation of a business case provides a point for managers to reject a proposal
before they allocate resources to a formal feasibility study. When evaluating software
development requests (and during subsequent feasibility and design analysis),
management should consider input from all affected parties. Management should also
closely evaluate the necessity of each requested functional requirement. A single
software feature approved during the initiation phase can require several design
documents and hundreds of lines of code. It can also increase testing, documentation,
and support requirements. Therefore, the initial rejection of unnecessary features can
significantly reduce the resources required to complete a project.

Planning Phase
The planning phase is the most critical step in completing development, acquisition, and
maintenance projects. Careful planning, particularly in the early stages of a project, is
necessary to coordinate activities and manage project risks effectively. The depth and
formality of project plans should be commensurate with the characteristics and risks of a
given project.
Project plans refine the information gathered during the initiation phase by further
identifying the specific activities and resources required to complete a project.

Design Phase
The design phase involves converting the informational, functional, and network
requirements identified during the initiation and planning phases into unified design
specifications that developers use to script programs during the development phase.
Program designs are constructed in various ways. Using a top-down approach,
designers first identify and link major program components and interfaces, then expand
design layouts as they identify and link smaller subsystems and connections. Using a
bottom-up approach, designers first identify and link minor program components and
interfaces, then expand design layouts as they identify and link larger systems and
connections.

Application Control Standards
Application controls include policies and procedures associated with user activities and
the automated controls designed into applications. Controls should be in place to
address both batch and on-line environments. Standards should address procedures to
ensure management appropriately approves and control overrides. Refer to the IT
Handbook's "Operations Booklet" for details relating to operational controls.
Designing appropriate security, audit, and automated controls into applications is a
challenging task. Often, because of the complexity of data flows, program logic, client/
server connections, and network interfaces, organizations cannot identify the exact type
and placement of the features until interrelated functions are identified in the design and
development phases. However, the security, integrity, and reliability of an application is
enhanced if management considers security, audit, and automated control features at
the onset of a project and includes them as soon as possible in application and system
designs. Adding controls late in the development process or when applications are in
production is more expensive, time consuming, and usually results in less effective
controls.

Development Phase
The development phase involves converting design specifications into executable
programs. Effective development standards include requirements that programmers and
other project participants discuss design specifications before programming begins. The
procedures help ensure programmers clearly understand program designs and
functional requirements.
Programmers use various techniques to develop computer programs. The large
transaction-oriented programs associated with financial institutions have traditionally
been developed using procedural programming techniques. Procedural programming
involves the line-by-line scripting of logical instructions that are combined to form a
program.

Development Standards
Development standards should be in place to address the responsibilities of application
and system programmers. Application programmers are responsible for developing and
maintaining end-user applications. System programmers are responsible for developing
and maintaining internal and open-source operating system programs that link
application programs to system software and subsequently to hardware. Managers
should thoroughly understand development and production environments to ensure they
appropriately assign programmer responsibilities.
Development standards should prohibit a programmer's access to data, programs,
utilities, and systems outside their individual responsibilities. Library controls can be used
to manage access to, and the movement of programs between, development, testing,
and production environments. Management should also establish standards requiring
programmers to document completed programs and test results thoroughly. Appropriate
documentation enhances a programmer's ability to correct programming errors and
modify production programs.
Coding standards, which address issues such as the selection of programming
languages and tools, the layout or format of scripted code, and the naming conventions
of code routines and program libraries, are outside the scope of this document. However,
standardized, yet flexible, coding standards enhance an organization's ability to
decrease coding defects and increase the security, reliability, and maintainability of
application programs. Examiners should evaluate an organization's coding standards
and related code review procedures.

Library Controls
Libraries are collections of stored documentation, programs, and data. Program libraries
include reusable program routines or modules stored in source or object code formats.
Program libraries allow programmers to access frequently used routines and add them to
programs without having to rewrite the code. Dynamic link libraries include executable
code programs can automatically run as part of larger applications.

Version Controls
Library controls facilitate software version controls. Version controls provide a means to
systematically retain chronological copies of revised programs and program
documentation.

Software Documentation
Organizations should maintain detailed documentation for each application and
application system in production. Thorough documentation enhances an organization's
ability to understand functional, security, and control features and improves its ability to
use and maintain the software. The documentation should contain detailed application
descriptions, programming documentation, and operating instructions. Standards should
be in place that identify the type and format of required documentation such as system
narratives, flowcharts, and any special system coding, internal controls, or file layouts not
identified within individual application documentation.

Testing Phase
The testing phase requires organizations to complete various tests to ensure the
accuracy of programmed code, the inclusion of expected functionality, and the
interoperability of applications and other network components. Thorough testing is critical
to ensuring systems meet organizational and end-user requirements.
If organizations use effective project management techniques, they will complete test
plans while developing applications, prior to entering the testing phase. Weak project
management techniques or demands to complete projects quickly may pressure
organizations to develop test plans at the start of the testing phase. Test plans created
during initial project phases enhance an organization's ability to create detailed tests.
The use of detailed test plans significantly increases the likelihood that testers will
identify weaknesses before products are implemented.

Implementation Phase
The implementation phase involves installing approved applications into production
environments. Primary tasks include announcing the implementation schedule, training
end users, and installing the product. Additionally, organizations should input and verify
data, configure and test system and security parameters, and conduct postimplementation reviews. Management should circulate implementation schedules to all
affected parties and should notify users of any implementation responsibilities.

"""

